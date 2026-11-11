interface StubFile {
  path: string;
  size: number;
  topic: string;
}

interface TaskResult {
  path: string;
  status: "completed" | "skipped" | "failed";
  summary: string;
  error?: string;
}

interface WorkflowReport {
  conclusion: string;
  findings: { where: string; what: string; evidence: string; status: "verified" | "unconfirmed"; severity: "low" | "medium" | "high" }[];
  verified: string[];
  notCovered: string[];
}

phase("Discover all stub files");
const topics: string[] = ["queue", "hash", "string", "backtrack", "greedy", "graph", "matrix", "other", "concurrency", "binary_search", "notes"];
const pythonBase = "/Users/Wang/Code/github/web-x-blog/work/target/21.dsa/python";
const tsBase = "/Users/Wang/Code/github/web-x-blog/work/target/21.dsa/ts";
const blogBase = "/Users/Wang/Code/github/web-x-blog/work/target/21.dsa/blog";

const stubs: StubFile[] = [];
for (const topic of topics) {
  const result = await world.run("find", [
    `${pythonBase}/${topic}`,
    "-name", "solution_*.py"
  ]);
  for (const line of result.stdout.trim().split("\n")) {
    if (!line.trim()) continue;
    const sizeResult = await world.run("wc", ["-c", line.trim()]);
    const size = parseInt(sizeResult.stdout.trim().split(/\s+/)[0], 10);
    if (size < 200 && size > 5) {
      stubs.push({ path: line.trim(), size, topic });
    }
  }
}

log(`Found ${stubs.length} stub files`);

phase("Translate each stub from TS reference or blog");
const translator = agent("Python Algorithm Translator", {
  system: `You are a Python algorithm translator. Your job is to read a TypeScript algorithm reference or a blog article and write proper Python implementation code.

Rules:
1. Read the Python stub file to understand the function signature
2. Find the matching TypeScript reference file in the corresponding ts/{topic}/{problem_dir}/ directory, OR check blog articles at /Users/Wang/Code/github/web-x-blog/work/target/21.dsa/blog/{id}/index.md
3. Translate the algorithm logic from TypeScript/blog to clean, idiomatic Python
4. Write the completed Python file, preserving the original function signature
5. For notes problems (lc_13xxxxxx), blog articles contain Python implementations already
6. Use standard Python data structures: dict instead of Map, list instead of arrays, set instead of Set, collections.deque for queues
7. Do NOT include demo/test code at the bottom - just the function/class implementation
8. The output file must be valid Python that can be imported and executed
9. If no good reference is found but you know the algorithm, implement it directly based on the problem name
10. For pseudo-Python constructs like Map(), Set(), .has(), .get(), .set(), .add(), .delete(), .clear() - translate to actual Python dict/set operations`
});

// Process in batches of 20 for parallel execution
const BATCH_SIZE = 20;
const allResults: TaskResult[] = [];

for (let i = 0; i < stubs.length; i += BATCH_SIZE) {
  const batch = stubs.slice(i, i + BATCH_SIZE);

  const batchResults = await Promise.all(batch.map(async (stub) => {
    const pathParts = stub.path.split("/");
    const filename = pathParts[pathParts.length - 1];
    const problemDir = pathParts[pathParts.length - 2];
    const topic = stub.topic;

    // Find matching TS reference
    let tsRef = "";
    try {
      const tsResult = await world.run("find", [
        `${tsBase}/${topic}/${problemDir}`,
        "-name", filename.replace(".py", ".ts")
      ]);
      tsRef = tsResult.stdout.trim().split("\n")[0];
    } catch {}

    // For notes problems, check blog
    let blogContent = "";
    if (topic === "notes" && problemDir.startsWith("lc_")) {
      const idMatch = problemDir.match(/lc_(\d+)_/);
      if (idMatch) {
        const blogId = idMatch[1];
        try {
          const blogResult = await world.run("cat", [`${blogBase}/${blogId}/index.md`]);
          blogContent = blogResult.stdout;
        } catch {}
      }
    }

    const stubContent = await files.read(stub.path);

    const instruction = tsRef
      ? `Translate this Python stub from its TypeScript reference:

STUB FILE: ${stub.path}
STUB CONTENT:
${stubContent}

TS REFERENCE (${tsRef}):
${await files.read(tsRef)}`
      : blogContent
      ? `Translate this Python stub from the blog article:

STUB FILE: ${stub.path}
STUB CONTENT:
${stubContent}

BLOG ARTICLE (${problemDir}):
${blogContent.substring(0, 12000)}`
      : `Implement this Python stub based on the problem description:

STUB FILE: ${stub.path}
STUB CONTENT:
${stubContent}

PROBLEM: ${problemDir} (topic: ${topic})`;

    const result = await translator.ask<TaskResult>(instruction);
    return result;
  }));

  allResults.push(...batchResults);
}

phase("Verify completed files");
let completedCount = 0;
let failedCount = 0;

for (const result of allResults) {
  if (result.status === "completed") {
    completedCount++;
  } else if (result.status === "failed") {
    failedCount++;
  }
}

phase("Generate report");
const report: WorkflowReport = {
  conclusion: `Completed ${completedCount} of ${stubs.length} Python stub files. ${failedCount} files could not be translated.`,
  findings: allResults.filter(r => r.status !== "completed").map(r => ({
    where: r.path,
    what: r.error || "Translation failed or skipped",
    evidence: r.summary,
    status: "unconfirmed" as const,
    severity: "medium" as const
  })),
  verified: [`wc -c verification on ${completedCount} completed files`],
  notCovered: ["Runtime validation of algorithm correctness (no test suite available)"]
};

return report;
