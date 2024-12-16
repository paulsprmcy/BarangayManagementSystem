from DBConnection import Connection
import bcrypt
from bcrypt import gensalt, checkpw

class Service:
    def __init__(self):
        self.con = None

    def start_connection(self):
        self.con = Connection()


    def get_streets(self):
        data = self.con.query("SELECT * FROM `streets`")
        return data
    def get_projects(self):
        # Query the database to get the list of projects
        try:
            query = "SELECT * FROM `projects`"
            data = self.con.query(query)  # Assuming `query` method returns a list of tuples or dictionaries
            return data
        except Exception as e:
            print(f"Error fetching projects: {e}")
            return []

    def update_funds(self, street, spend):
        try:
            # Fetch the current funds for the street
            query = "SELECT `funds` FROM `streets` WHERE `street` = %s"
            current_funds = self.con.query(query, (street,))
            if current_funds:
                new_funds = current_funds[0][0] - spend  # Decrease the funds by the project's spend
                # Update the funds in the database
                query = "UPDATE `streets` SET `funds` = %s WHERE `street` = %s"
                values = (new_funds, street)
                self.con.query(query, values)
                self.con.connection.commit()
                return ("Success", f"Funds updated successfully for street {street}")
            else:
                return("Error", f"Street {street} not found.")
        except Exception as e:
            return("Error", f"Error updating funds: {e}")

    def add_funds(self, street, add):
        try:
            # Fetch the current funds for the street
            query = "SELECT `funds` FROM `streets` WHERE `street` = %s"
            current_funds = self.con.query(query, (street,))
            if current_funds:
                new_funds = current_funds[0][0] + add  # Decrease the funds by the project's spend
                # Update the funds in the database
                query = "UPDATE `streets` SET `funds` = %s WHERE `street` = %s"
                values = (new_funds, street)
                self.con.query(query, values)
                self.con.connection.commit()
                return ("Success", f"Funds updated successfully for street {street}")
            else:
                return ("Error", f"Street {street} not found.")
        except Exception as e:
            return ("Error", f"Error updating funds: {e}")

    def mark_project_as_done(self, project_id):
        try:
            # Update the project status to 'done' in the database
            query = "UPDATE `projects` SET `status` = 'done' WHERE `id` = %s"
            self.con.query(query, (project_id,))
            self.con.connection.commit()
            return("Success", f"Project marked as done.")
        except Exception as e:
            return("Error", f"Error updating project status: {e}")

    def add_street_needs(self, street, need, service):
        try:
            query = "INSERT INTO `needs` (`street`, `need`, `service`,`date`) VALUES (%s, %s, %s,NOW())"
            values = (street, need, service)
            self.con.query(query, values)
            self.con.connection.commit()
            return "Street needs added successfully."
        except Exception as e:
            return f"Error adding street needs: {e}"

    def get_needs(self):
        data = self.con.query("SELECT * FROM `needs`")
        return data

    def update_status(self,need_id):
        try:
            query = "UPDATE `needs` SET `status` = %s WHERE `id` = %s"
            values = ("Done", need_id)
            self.con.query(query, values)
            return f"Status updated successfully{need_id}"
        except Exception as e:
            return f"Error updating status: {e}"

    def set_priority(self, _street):
        try:
            print("*************",_street)
            query = "UPDATE `needs` SET `priority` = %s WHERE `street` = %s"
            values = (1, _street)
            self.con.query(query, values)
            return f"Prioritize successfully {_street}"
        except Exception as e:
            return f"Error: {e}"

    def add_projects(self, street, project, spend, service, area):
        try:
            print(street, project, spend, service, area)
            query = "INSERT INTO `projects` (`street`, `project`, `spend`, `service`, `area`,`date`) VALUES (%s, %s, %s, %s,%s,NOW())"
            values = (street, project, spend, service, area)
            self.con.query(query, values)
            self.con.connection.commit()
            return "Street projects added successfully."
        except Exception as e:
            return f"Error: {e}"
    def is_connected(self):
        return self.con.check_connection()

    def get_users(self):
        data = self.con.query("SELECT * FROM `users`")
        return data
    def register(self, username, password):
        try:
            # Properly hash the password
            hashed_password = password
            query = "INSERT INTO `users` (`username`, `password`) VALUES (%s, %s)"
            values = (username, hashed_password)
            self.con.query(query, values)
            self.con.connection.commit()
            return "User registered successfully."
        except Exception as e:
            return f"Error during registration: {e}"

    def login(self, username, password):
        try:
            query = "SELECT `password` FROM `users` WHERE `username` = %s"
            values = (username,)
            result = self.con.query(query, values)

            if result:
                stored_password = result[0][0]
                if isinstance(stored_password, str):
                    stored_password = stored_password

                if password == stored_password:
                    print("Login successful.")
                    return True
                else:
                    print("Invalid username or password.")
                    return False
            else:
                print("User not found.")
                return False
        except Exception as e:
            print(f"Error during login: {e}")
            return False

