// list all documents with name starting by Holberton in the collection school

db.school.find({name: {$regex: /^Holberton/}})
