from flask import Flask, request
from pymongo import MongoClient
from bson import ObjectId
from config import MONGO_URI

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient(MONGO_URI)
print("MongoDB URI loaded:", MONGO_URI[:20] if MONGO_URI else "NOT LOADED")
# Select database
db = client["smart_helpdesk"]

# Select collection
tickets_collection = db["tickets"]


@app.route("/")
def home():
    return "Smart Helpdesk is running!"
@app.route("/api/tickets", methods=["POST"])
def create_ticket():
    data = request.json

    ticket = {
        "title": data.get("title"),
        "description": data.get("description"),
        "priority": data.get("priority", "Medium"),
        "category": data.get("category", "General"),
        "status": "Open"
    }

    result = tickets_collection.insert_one(ticket)

    return {
        "message": "Ticket created successfully",
        "ticket_id": str(result.inserted_id)
    }, 201
@app.route("/api/tickets", methods=["GET"])
def get_tickets():
    tickets = []

    for ticket in tickets_collection.find():
        ticket["_id"] = str(ticket["_id"])
        tickets.append(ticket)

    return tickets, 200
@app.route("/api/tickets/<ticket_id>", methods=["PUT"])
def update_ticket(ticket_id):
    data = request.json

    update_data = {}

    if "status" in data:
        update_data["status"] = data["status"]

    if "priority" in data:
        update_data["priority"] = data["priority"]

    tickets_collection.update_one(
        {"_id": ObjectId(ticket_id)},
        {"$set": update_data}
    )

    return {
        "message": "Ticket updated successfully"
    }, 200
@app.route("/api/tickets/<ticket_id>", methods=["DELETE"])
def delete_ticket(ticket_id):
    result = tickets_collection.delete_one(
        {"_id": ObjectId(ticket_id)}
    )

    return {
        "message": "Ticket deleted successfully"
    }, 200
@app.route("/test-db")
def test_db():
    try:
        client.admin.command("ping")
        return "MongoDB connection successful!"
    except Exception as e:
        return f"MongoDB connection failed: {e}"

if __name__ == "__main__":
    app.run(debug=True)