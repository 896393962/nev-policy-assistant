const fs = require("node:fs");
const path = require("node:path");

if (process.platform === "win32") {
  process.exit(0);
}

const binDir = path.join(__dirname, "..", "node_modules", ".bin");

if (!fs.existsSync(binDir)) {
  process.exit(0);
}

for (const entry of fs.readdirSync(binDir)) {
  const target = path.join(binDir, entry);

  try {
    const stat = fs.statSync(target);
    fs.chmodSync(target, stat.mode | 0o755);
  } catch {
    // Best-effort compatibility with the previous shell postinstall hook.
  }
}
