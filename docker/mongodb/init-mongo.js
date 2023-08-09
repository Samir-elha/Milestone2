db = db.getSiblingDB('users'); // Create or switch to the database
db.createCollection('myCollection'); // Create a collection
db.myCollection.insert({ name: 'Samir EL-Hajjoui' }); // Insert a document