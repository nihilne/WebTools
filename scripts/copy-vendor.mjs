import { copyFileSync, mkdirSync } from "node:fs";
import { basename, join, resolve } from "node:path";

const root = resolve(import.meta.dirname, "..");
const dest = join(root, "app", "static", "js");

const files = [
  "node_modules/htmx.org/dist/htmx.min.js",
  "node_modules/sortablejs/Sortable.min.js",
];

mkdirSync(dest, { recursive: true });

for (const file of files) {
  copyFileSync(join(root, file), join(dest, basename(file)));
  console.log(`copied ${file} -> app/static/js/${basename(file)}`);
}
