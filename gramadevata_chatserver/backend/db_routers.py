class RegisterRouter:
    """
    A router to control all database operations on models in the
    gramadevata_updated1 database.
    """

    MODELS_IN_GRAMADEVATA_DB = {"Register", "Village", "Temple"}

    def db_for_read(self, model, **hints):
        """Route read operations"""
        if model.__name__ in self.MODELS_IN_GRAMADEVATA_DB:
            return 'gramadevata_updated1'
        return 'default'

    def db_for_write(self, model, **hints):
        """Route write operations"""
        if model.__name__ in self.MODELS_IN_GRAMADEVATA_DB:
            return 'gramadevata_updated1'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """Allow relations between models in different databases"""
        db_set = {obj1._state.db, obj2._state.db}
        if 'gramadevata_updated1' in db_set and 'default' in db_set:
            return True  # Allow relations
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Prevent migrations for Register, Village, and Temple in chat_server"""
        if model_name in self.MODELS_IN_GRAMADEVATA_DB:
            return db == "gramadevata_updated1"
        return db == "default"
