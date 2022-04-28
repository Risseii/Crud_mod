from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def muestra_usuarios(cls):
        query = "SELECT * FROM users"
        results = connectToMySQL('esquema_usuarios').query_db(query) #que me ejecute el query
        users = []
        for u in results:
            users.append(cls(u)) #forzando que sea de la clase users
        return users

    @classmethod
    def guardar(cls,formulario):
        #data = {"first_name": "C", "last_name": "X", "email": "c@cd.com"}
        query = "INSERT INTO users (first_name,last_name,email) VALUES (%(first_name)s,%(last_name)s,%(email)s)" 
        result = connectToMySQL("esquema_usuarios").query_db(query,formulario)
        return result
    
    @classmethod
    def borrar(cls,formulario):
        #formulario = {"id":"1"}
        query = "DELETE FROM users WHERE id=%(id)s"
        result = connectToMySQL("esquema_usuarios").query_db(query,formulario) 
        return result
    
    @classmethod
    def mostrar(cls,formulario):
        #formulario = {"id":"1"}
        query = "SELECT * FROM users WHERE id = %(id)s"
        result = connectToMySQL("esquema_usuarios").query_db(query,formulario)
        usr = result[0]
        user = cls(usr)
        return user 
    
    @classmethod
    def actualizar(cls,formulario):
        query = "UPDATE users SET first_name = %(first_name)s,last_name = %(last_name)s,email = %(email)s WHERE id = %(id)s"
        result = connectToMySQL("esquema_usuarios").query_db(query,formulario)
        return result
    
    


    