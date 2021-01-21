import redis from "redis";
const client = redis.createClient();

client.on("success", () => {
  console.log('Redis client connected to the server');
});

client.on("error", (error) => {
  console.log(`Redis client not connected to the server: ${error}`);
});
