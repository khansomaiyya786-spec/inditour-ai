from pymongo import MongoClient

# Replace with your actual MongoDB Atlas connection string
MONGO_URI = "mongodb+srv://username:password@inditour-ai.mongodb.net"

client = MongoClient(MONGO_URI)
db = client["inditour_ai_db"]

# Collections
destinations_col = db["destinations"]
users_col        = db["users"]
hotels_col       = db["hotels"]
bookings_col     = db["bookings"]

print("✅ Connected to MongoDB Atlas!")