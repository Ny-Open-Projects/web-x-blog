import ExcelJs from "exceljs";
import JSZip from "jszip";

// 生成表格的表头
function generateHeader(columns: any[]) {
  return columns.map((col) => ({
    // 列头显示文字
    header: col.title,
    // 用于数据匹配的 key
    key: col.dataIndex,
    // 列宽
    width: 20,
  }));
}

/**
 * 将buffer保存成Blob大对象文件
 */
async function saveFile(buffer: any, fileName: string) {
  const blob = new Blob([buffer], { type: "application/octet-stream" });
  saveFileWithBlob(blob, fileName);
}

/**
 * 将Blob保存成文件
 */
async function saveFileWithBlob(blob: Blob, fileName: string) {
  const link = document.createElement("a");
  link.href = window.URL.createObjectURL(blob);
  link.download = fileName;
  link.click();
  window.URL.revokeObjectURL(link.href);
}

/**
 * 将json数据转换为Excel文件
 */
export async function jsonToExcel(options: {
  columns: any[];
  dataSource: any[];
  title: string;
  isWriteFile?: boolean;
}) {
  const { columns, dataSource, title, isWriteFile = true } = options;

  // 创建工作簿
  const workbook = new ExcelJs.Workbook();
  // 添加工作表
  const worksheet = workbook.addWorksheet(title);
  // 设置默认行高
  worksheet.properties.defaultRowHeight = 20;
  // 生成表头
  worksheet.columns = generateHeader(columns);
  // 添加行数据
  worksheet.addRows(dataSource);

  // 生成Excel文件的缓冲区
  const buffer = await workbook.xlsx.writeBuffer();

  // 如果需要写入文件，则保存文件
  if (isWriteFile) await saveFile(buffer, `${title}-数据统计.xlsx`);

  // 返回结果
  return {
    buffer,
    title: `${title}-数据统计`,
  };
}

/**
 * 将Excel文件转换为ZIP文件
 */
export async function excelToZip(params: { buffer: any; title: string }) {
  const { buffer, title } = params;

  // 创建一个新的JSZip实例
  const jszip = new JSZip();

  // 添加Excel文件到JSZip实例中
  jszip.file(`${title}.xlsx`, buffer);

  // 生成ZIP文件的Blob对象
  const blob = await jszip.generateAsync({ type: "blob" });

  // 保存ZIP文件
  saveFileWithBlob(blob, `${title}.zip`);
}
