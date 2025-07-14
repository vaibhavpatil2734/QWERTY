const express = require("express");
const fs = require("fs");
const cors = require("cors");
const app = express();
const port = process.env.PORT || 3000;

app.use(cors());
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.post("/receive_logs", (req, res) => {
  const logData = req.body.log;

  if (!logData) {
    return res.status(400).send("No log data received");
  }

  fs.appendFile("received_logs.txt", logData + "\n", (err) => {
    if (err) {
      console.error("Error writing log file:", err);
      return res.status(500).send("Error saving log");
    }
    console.log("Log data received and saved.");
    res.status(200).send("Log received");
  });
});

app.get("/", (req, res) => {
  res.send("Log receiver is running.");
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
