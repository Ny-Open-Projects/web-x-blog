import { getBoard } from "@/lib/market";
import Board from "@/components/Board";

export const revalidate = 60;

export default async function Page() {
  let initial = null;
  try { initial = await getBoard(); } catch { initial = null; }
  return <Board initial={initial} />;
}
