import uuid

import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError


def create_recipe_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.create_table(
        TableName='Recipes',
        KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'  # Partition key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )

    return table


def load_sample_recipes(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('Recipes')

    recipes = [
        {
            'id': str(uuid.uuid4()),
            'name': 'Spaghetti Bolognese',
            'posterId': '123',
            'imageURL': 'https://www.slimmingeats.com/blog/wp-content/uploads/2010/04/spaghetti-bolognese-36-720x720.jpg',
            'content': 'Delicious spaghetti with a rich Bolognese sauce.'
        },
        {
            'id': str(uuid.uuid4()),
            'name': 'Chicken Curry',
            'posterId': '124',
            'imageURL': 'https://www.foodandwine.com/thmb/8YAIANQTZnGpVWj2XgY0dYH1V4I=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/spicy-chicken-curry-FT-RECIPE0321-58f84fdf7b484e7f86894203eb7834e7.jpg',
            'content': 'Aromatic chicken curry with a blend of spices.'
        },
        {
            'id': str(uuid.uuid4()),
            'name': 'Beef Stew',
            'posterId': '125',
            'imageURL': 'https://s23209.pcdn.co/wp-content/uploads/2020/03/Best-Ever-Beef-StewIMG_1367.jpg',
            'content': 'Hearty beef stew with tender pieces of beef and vegetables.'
        },
        {
            'id': str(uuid.uuid4()),
            'name': 'Lanzhou Beef Noodles',
            'posterId': '125',
            'imageURL': 'https://thewoksoflife.com/wp-content/uploads/2014/10/lanzhou-beef-noodle-soup-6.jpg',
            'content': """
### Ingredients

#### For the Broth:
- 2 lbs (1 kg) beef bones
- 1 lb (500 g) beef shank or brisket
- 10 cups water
- 3 slices ginger
- 3 green onions (cut into 2-inch pieces)
- 2 star anise
- 1 cinnamon stick
- 3 bay leaves
- 1 black cardamom pod
- 1 tsp Sichuan peppercorns
- 1 dried chili pepper (optional)
- Salt to taste

#### For the Noodles:
- 500 g (1 lb) high-gluten flour
- 250 ml (1 cup) water
- 1 tsp salt

#### Toppings:
- 1 bunch fresh cilantro (chopped)
- 2 green onions (finely chopped)
- 1-2 red chili peppers (sliced thin)
- Pickled garlic (optional)
- White radish (thinly sliced)
- Chili oil (optional)

### Instructions

#### Preparing the Broth:

1. **Blanch the Bones and Meat**: Place the beef bones and beef shank in a large pot, cover with cold water, and bring to a boil. Boil for about 5 minutes, then drain and rinse the bones and meat under cold water to remove impurities.

2. **Simmer the Broth**: Return the bones and beef shank to the pot, add 10 cups of water, ginger slices, green onions, star anise, cinnamon stick, bay leaves, black cardamom pod, Sichuan peppercorns, and dried chili pepper (if using). Bring to a boil, then reduce to a simmer. Cover and simmer for at least 3 hours, skimming any foam or impurities that rise to the surface.

3. **Season the Broth**: After simmering, remove the beef shank, strain the broth to remove the solids, and season with salt to taste. Slice the beef shank thinly for serving.

#### Making the Noodles:

1. **Prepare the Dough**: In a large mixing bowl, combine the high-gluten flour and salt. Gradually add the water, mixing until a rough dough forms. Knead the dough for about 10-15 minutes until it becomes smooth and elastic.

2. **Rest the Dough**: Cover the dough with a damp cloth and let it rest for at least 1 hour.

3. **Form the Noodles**: Divide the dough into small portions and roll each portion into a long, thin rope. Use your hands to pull and stretch the dough ropes to form long noodles, or use a pasta machine if available.

#### Cooking and Serving:

1. **Cook the Noodles**: Bring a large pot of water to a boil. Add the freshly pulled noodles and cook for 2-3 minutes, or until they float to the surface and are cooked through. Drain the noodles and rinse under cold water.

2. **Assemble the Bowl**: Place a portion of cooked noodles in a bowl. Top with slices of beef shank, thinly sliced white radish, chopped cilantro, green onions, and red chili peppers. Ladle hot beef broth over the noodles and add pickled garlic and chili oil if desired.

3. **Serve**: Enjoy your Lanzhou Beef Noodles hot, with additional chili oil and pickled garlic on the side if you like.

### Tips:
- The key to authentic Lanzhou Beef Noodles is the clear and aromatic broth, so take your time to simmer the broth and ensure it's well-seasoned.
- Freshly made noodles have a better texture, but you can use store-bought noodles if you're short on time.
- Customize your bowl with different toppings based on your preference.
"""
        }
    ]

    for recipe in recipes:
        try:
            table.put_item(Item=recipe)
            print(f"Inserted recipe: {recipe['name']}")
        except (NoCredentialsError, PartialCredentialsError) as e:
            print(f"Credentials error: {e}")
        except Exception as e:
            print(f"Error inserting recipe: {e}")


if __name__ == '__main__':
    recipe_table = create_recipe_table()
    print("Table status:", recipe_table.table_status)

    load_sample_recipes()
