class Contact:
    '''
    Contact class to represent a contact with a name and number.
    Attributes:
        name (str): The name of the contact.
        number (str): The phone number of the contact.
    '''
    
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"{self.name}: {self.number}"

class Node:
    '''
    Node class to represent a single entry in the hash table.
    Attributes:
        key (str): The key (name) of the contact.
        value (Contact): The value (Contact object) associated with the key.
        next (Node): Pointer to the next node in case of a collision.
    '''
   
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)

class HashTable:
    '''
    HashTable class to represent a hash table for storing contacts.
    Attributes:
        size (int): The size of the hash table.
        data (list): The underlying array to store linked lists for collision handling.
    Methods:
        hash_function(key): Converts a string key into an array index.
        insert(key, value): Inserts a new contact into the hash table.
        search(key): Searches for a contact by name.
        print_table(): Prints the structure of the hash table.
    '''
    
    def __init__(self, size):
        self.size = size
        self.data = [None] * size

    def hash_function(self, key):
        total = 0
        for char in key:
            total += ord(char)
        return total % self.size
    
    def insert(self, key, number):
        index = self.hash_function(key)
        new_contact = Contact(key, number)
        new_node = Node(key, new_contact)

        if self.data[index] is None:
            self.data[index] = new_node
        else:
            current = self.data[index]
            while current is not None:
                if current.key == key:
                    current.value.number = number
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = new_node

    def search(self, key):
        index = self.hash_function(key)
        current = self.data[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None
    
    def print_table(self):
        for i in range(self.size):
            print(f"Index {i}:", end=" ")
            if self.data[i] is None:
                print("Empty")
            else:
                current = self.data[i]
                while current:
                    print(f"- {current.value}", end=" ")
                    current = current.next
                print()

# Test your hash table implementation here.  
table = HashTable(10)

#Prints the initial (empty) table
print("Initial Table:")
table.print_table()

#Inserting the contacts
print("\nInserting contacts...")
table.insert("John", "909-876-1234")
table.insert("Rebecca", "111-555-0002")
table.insert("Amy", "111-222-3333")
table.insert("May", "222-333-1111")

#Printing table with the new insertions
print("\nTable after insertions:")
table.print_table()

#Searching for an existing contact
print("\nSearching for John:")
contact = table.search("John")
print("Result:", contact)

#Searching for nonexistant contact
print("\nSearching for Chris:")
contact = table.search("Chris")
print("Result:", contact)

#Updating an existing contact
print("\nUpdating Rebecca's number...")
table.insert("Rebecca", "999-444-9999")

#Printing the final table with fixes
print("\nFinal Table:")
table.print_table()