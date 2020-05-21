from types import MethodType
from django.test.runner import DiscoverRunner
from django.db import connections


def prepare_database(self):
    self.connect()
    self.connection.cursor().execute(
        """
    CREATE SCHEMA content AUTHORIZATION admin;
    GRANT ALL ON SCHEMA content TO admin;
    """
    )


class PostgresSchemaTestRunner(DiscoverRunner):
    def setup_databases(self, **kwargs):
        for connection_name in connections:
            connection = connections[connection_name]
            connection.prepare_database = MethodType(prepare_database, connection)
        return super().setup_databases(**kwargs)
