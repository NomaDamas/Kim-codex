const http = require("http");
const fs = require("fs");
const path = require("path");
const { spawn } = require("child_process");

const root = __dirname;
const port = Number(process.env.PORT || 4173);
const host = process.env.HOST || "127.0.0.1";

const mime = {
  ".html": "text/html; charset=utf-8",
  ".css": "text/css; charset=utf-8",
  ".js": "text/javascript; charset=utf-8",
  ".json": "application/json; charset=utf-8",
  ".svg": "image/svg+xml; charset=utf-8"
};

function sendJson(res, status, payload) {
  res.writeHead(status, {
    "content-type": "application/json; charset=utf-8",
    "cache-control": "no-store"
  });
  res.end(JSON.stringify(payload, null, 2));
}

function runPythonScript(scriptName, res) {
  const scriptPath = path.join(root, "scripts", scriptName);
  const child = spawn("python3", [scriptPath], {
    cwd: root,
    env: { ...process.env, PYTHONUNBUFFERED: "1" }
  });
  let stdout = "";
  let stderr = "";

  child.stdout.on("data", (chunk) => {
    stdout += chunk.toString();
  });
  child.stderr.on("data", (chunk) => {
    stderr += chunk.toString();
  });
  child.on("error", (error) => {
    sendJson(res, 500, { ok: false, error: error.message });
  });
  child.on("close", (code) => {
    try {
      const lines = stdout.trim().split(/\r?\n/).filter(Boolean);
      const jsonLine = [...lines].reverse().find((line) => line.trim().startsWith("{")) || "{}";
      const payload = JSON.parse(jsonLine);
      sendJson(res, code === 0 ? 200 : 500, payload);
    } catch (error) {
      sendJson(res, 500, {
        ok: false,
        error: "Python script did not return JSON.",
        stderr,
        stdout
      });
    }
  });
}

const server = http.createServer((req, res) => {
  const urlPath = decodeURIComponent(new URL(req.url, `http://localhost:${port}`).pathname);

  if (urlPath === "/api/sc2-run") {
    runPythonScript("sc2_codex_bot.py", res);
    return;
  }

  if (urlPath === "/api/sc2-real") {
    runPythonScript("sc2_real_game.py", res);
    return;
  }

  if (urlPath === "/api/progeny-run") {
    runPythonScript("progeny_lab.py", res);
    return;
  }

  const safePath = urlPath === "/" ? "/index.html" : urlPath;
  const filePath = path.join(root, safePath);

  if (!filePath.startsWith(root)) {
    res.writeHead(403);
    res.end("Forbidden");
    return;
  }

  fs.readFile(filePath, (error, data) => {
    if (error) {
      res.writeHead(404);
      res.end("Not found");
      return;
    }

    res.writeHead(200, {
      "content-type": mime[path.extname(filePath)] || "application/octet-stream",
      "cache-control": "no-store"
    });
    res.end(data);
  });
});

server.listen(port, host, () => {
  console.log(`Happy Codex MVP: http://${host}:${port}`);
});
