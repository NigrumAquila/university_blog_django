from django_seed import Seed
from ..models import Post

seeder = Seed.seeder()

seeder.add_entity(Post, 1, {
    'name': lambda x: seeder.faker.email(),
})
seeder.execute()