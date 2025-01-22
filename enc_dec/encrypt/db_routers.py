class RawDataRouter:
    """
    A database router to direct read/write operations for `RawUserData` model to `raw_db`.
    """

    def db_for_read(self, model, **hints):
        """
        Attempts to read `RawUserData` models go to `raw_db`.
        """
        if model._meta.app_label == 'encrypt' and model.__name__ == 'RawUserData':
            return 'raw_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write `RawUserData` models go to `raw_db`.
        """
        if model._meta.app_label == 'encrypt' and model.__name__ == 'RawUserData':
            return 'raw_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Determines if a relation between two models is allowed.
        """
        if obj1._meta.app_label == 'encrypt' and obj2._meta.app_label == 'encrypt':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Prevents the `RawUserData` model from being migrated in the default database.
        """
        if app_label == 'encrypt' and model_name == 'rawuserdata':
            return db == 'raw_db'
        return None
