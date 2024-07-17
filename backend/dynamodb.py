import uuid
import os
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError


def create_recipe_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource(
            'dynamodb',
            endpoint_url="http://dynamodb:8000",
            region_name="us-west-2",
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
        )

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
        dynamodb = boto3.resource(
            'dynamodb',
            endpoint_url="http://dynamodb:8000",
            region_name="us-west-2",
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
        )

    table = dynamodb.Table('Recipes')

    recipes = [
        {
            "id": str(uuid.uuid4()),
            "name": "Spaghetti Bolognese",
            "posterId": "123",
            "imageURL": "https://www.slimmingeats.com/blog/wp-content/uploads/2010/04/spaghetti-bolognese-36-720x720.jpg",
            "content": "<h3 style=\"-webkit-text-stroke-width:0px;caret-color:rgb(0, 0, 0);color:rgb(0, 0, "
                       "0);font-style:normal;font-variant-caps:normal;letter-spacing:normal;orphans:auto;text-align"
                       ":start;text-decoration:none;text-indent:0px;text-transform:none;white-space:normal;widows"
                       ":auto;word-spacing:0px;\">Spaghetti Bolognese Recipe</h3><h4 "
                       "style=\"-webkit-text-stroke-width:0px;caret-color:rgb(0, 0, 0);color:rgb(0, 0, "
                       "0);font-style:normal;font-variant-caps:normal;letter-spacing:normal;orphans:auto;text-align"
                       ":start;text-decoration:none;text-indent:0px;text-transform:none;white-space:normal;widows"
                       ":auto;word-spacing:0px;\">Ingredients:</h4><ul "
                       "style=\"-webkit-text-stroke-width:0px;caret-color:rgb(0, 0, 0);color:rgb(0, 0, "
                       "0);font-style:normal;font-variant-caps:normal;font-weight:400;letter-spacing:normal;orphans"
                       ":auto;text-align:start;text-decoration:none;text-indent:0px;text-transform:none;white-space"
                       ":normal;widows:auto;word-spacing:0px;\"><li>1 pound ground beef</li><li>1 large onion, "
                       "chopped</li><li>2 cloves garlic, minced</li><li>1 carrot, grated</li><li>1 celery stalk, "
                       "chopped</li><li>1 can (28 ounces) crushed tomatoes</li><li>1/4 cup tomato paste</li><li>1/2 "
                       "cup red wine (optional)</li><li>1 cup beef broth</li><li>1 teaspoon dried basil</li><li>1 "
                       "teaspoon dried oregano</li><li>Salt and pepper to taste</li><li>1 pound "
                       "spaghetti</li><li>Freshly grated Parmesan cheese for serving</li></ul><h4 "
                       "style=\"-webkit-text-stroke-width:0px;caret-color:rgb(0, 0, 0);color:rgb(0, 0, "
                       "0);font-style:normal;font-variant-caps:normal;letter-spacing:normal;orphans:auto;text-align"
                       ":start;text-decoration:none;text-indent:0px;text-transform:none;white-space:normal;widows"
                       ":auto;word-spacing:0px;\">Instructions:</h4><ol "
                       "style=\"-webkit-text-stroke-width:0px;caret-color:rgb(0, 0, 0);color:rgb(0, 0, "
                       "0);font-style:normal;font-variant-caps:normal;font-weight:400;letter-spacing:normal;orphans"
                       ":auto;text-align:start;text-decoration:none;text-indent:0px;text-transform:none;white-space"
                       ":normal;widows:auto;word-spacing:0px;\"><li><strong>Prepare the Meat "
                       "Sauce:</strong><ul><li>In a large pot, cook the ground beef over medium heat until browned. "
                       "Drain excess fat.</li><li>Add chopped onion, garlic, carrot, and celery to the pot. Cook "
                       "until vegetables are tender, about 5-7 minutes.</li><li>Stir in crushed tomatoes, "
                       "tomato paste, red wine (if using), and beef broth. Add basil, oregano, salt, and pepper. "
                       "Bring to a boil, then reduce heat and simmer for 30-40 minutes, stirring "
                       "occasionally.</li></ul></li><li><strong>Cook the Spaghetti:</strong><ul><li>While the sauce "
                       "is simmering, cook the spaghetti according to package instructions. Drain and set "
                       "aside.</li></ul></li><li><strong>Combine and Serve:</strong><ul><li>Serve the meat sauce over "
                       "the cooked spaghetti. Top with freshly grated Parmesan cheese.</li></ul></li></ol><p "
                       "style=\"-webkit-text-stroke-width:0px;caret-color:rgb(0, 0, 0);color:rgb(0, 0, "
                       "0);font-style:normal;font-variant-caps:normal;font-weight:400;letter-spacing:normal;orphans"
                       ":auto;text-align:start;text-decoration:none;text-indent:0px;text-transform:none;white-space"
                       ":normal;widows:auto;word-spacing:0px;\">Delicious spaghetti with a rich Bolognese sauce.</p>"
        },
        {
            "id": str(uuid.uuid4()),
            "name": "Beef Stew",
            "posterId": "yuqi.guo17@gmail.com",
            "imageURL": "https://s23209.pcdn.co/wp-content/uploads/2020/03/Best-Ever-Beef-StewIMG_1367.jpg",
            "content": "<h3 style=\"-webkit-text-stroke-width:0px;caret-color:rgb(0, 0, 0);color:rgb(0, 0, "
                       "0);font-style:normal;font-variant-caps:normal;letter-spacing:normal;orphans:auto;text-align"
                       ":start;text-decoration:none;text-indent:0px;text-transform:none;white-space:normal;widows"
                       ":auto;word-spacing:0px;\">Beef Stew Recipe</h3><h4 "
                       "style=\"-webkit-text-stroke-width:0px;caret-color:rgb(0, 0, 0);color:rgb(0, 0, "
                       "0);font-style:normal;font-variant-caps:normal;letter-spacing:normal;orphans:auto;text-align"
                       ":start;text-decoration:none;text-indent:0px;text-transform:none;white-space:normal;widows"
                       ":auto;word-spacing:0px;\">Ingredients:</h4><ul "
                       "style=\"-webkit-text-stroke-width:0px;caret-color:rgb(0, 0, 0);color:rgb(0, 0, "
                       "0);font-style:normal;font-variant-caps:normal;font-weight:400;letter-spacing:normal;orphans"
                       ":auto;text-align:start;text-decoration:none;text-indent:0px;text-transform:none;white-space"
                       ":normal;widows:auto;word-spacing:0px;\"><li>2 pounds beef stew meat, cut into 1-inch "
                       "cubes</li><li>1/4 cup all-purpose flour</li><li>1/2 teaspoon salt</li><li>1/2 teaspoon black "
                       "pepper</li><li>2 tablespoons olive oil</li><li>1 large onion, chopped</li><li>3 cloves "
                       "garlic, minced</li><li>4 cups beef broth</li><li>1 cup red wine (optional)</li><li>3 large "
                       "carrots, peeled and sliced</li><li>4 large potatoes, peeled and cubed</li><li>2 stalks "
                       "celery, sliced</li><li>1 tablespoon tomato paste</li><li>1 teaspoon dried thyme</li><li>1 "
                       "teaspoon dried rosemary</li><li>1 bay leaf</li><li>1 cup frozen peas</li><li>1/4 cup chopped "
                       "fresh parsley</li></ul><h4 style=\"-webkit-text-stroke-width:0px;caret-color:rgb(0, 0, "
                       "0);color:rgb(0, 0, "
                       "0);font-style:normal;font-variant-caps:normal;letter-spacing:normal;orphans:auto;text-align"
                       ":start;text-decoration:none;text-indent:0px;text-transform:none;white-space:normal;widows"
                       ":auto;word-spacing:0px;\">Instructions:</h4><ol "
                       "style=\"-webkit-text-stroke-width:0px;caret-color:rgb(0, 0, 0);color:rgb(0, 0, "
                       "0);font-style:normal;font-variant-caps:normal;font-weight:400;letter-spacing:normal;orphans"
                       ":auto;text-align:start;text-decoration:none;text-indent:0px;text-transform:none;white-space"
                       ":normal;widows:auto;word-spacing:0px;\"><li><strong>Prepare the Meat:</strong><ul><li>In a "
                       "large bowl, combine the flour, salt, and pepper. Add the beef cubes and toss to coat "
                       "evenly.</li></ul></li><li><strong>Brown the Meat:</strong><ul><li>In a large pot or Dutch "
                       "oven, heat the olive oil over medium-high heat. Add the beef cubes in batches, browning them "
                       "on all sides. Remove the beef from the pot and set aside.</li></ul></li><li><strong>Sauté the "
                       "Vegetables:</strong><ul><li>In the same pot, add the chopped onion and sauté until softened, "
                       "about 5 minutes. Add the minced garlic and cook for an additional "
                       "minute.</li></ul></li><li><strong>Deglaze the Pot:</strong><ul><li>Pour in the red wine (if "
                       "using) and stir, scraping up any browned bits from the bottom of the pot. Allow the wine to "
                       "simmer for a few minutes until it reduces slightly.</li></ul></li><li><strong>Add Broth and "
                       "Seasonings:</strong><ul><li>Return the browned beef to the pot. Add the beef broth, "
                       "tomato paste, thyme, rosemary, and bay leaf. Stir to combine.</li></ul></li><li><strong>Cook "
                       "the Stew:</strong><ul><li>Bring the mixture to a boil, then reduce the heat to low. Cover the "
                       "pot and let it simmer for 1.5 to 2 hours, or until the beef is "
                       "tender.</li></ul></li><li><strong>Add Vegetables:</strong><ul><li>Add the carrots, potatoes, "
                       "and celery to the pot. Continue to simmer for another 30 minutes, or until the vegetables are "
                       "tender.</li></ul></li><li><strong>Final Touches:</strong><ul><li>Stir in the frozen peas and "
                       "let them cook for 5 minutes. Remove the bay leaf and "
                       "discard.</li></ul></li><li><strong>Serve:</strong><ul><li>Taste and adjust the seasoning with "
                       "salt and pepper if needed. Garnish with fresh parsley before serving.</li></ul></li></ol><p "
                       "style=\"-webkit-text-stroke-width:0px;caret-color:rgb(0, 0, 0);color:rgb(0, 0, "
                       "0);font-style:normal;font-variant-caps:normal;font-weight:400;letter-spacing:normal;orphans"
                       ":auto;text-align:start;text-decoration:none;text-indent:0px;text-transform:none;white-space"
                       ":normal;widows:auto;word-spacing:0px;\">Enjoy your delicious homemade beef stew!</p>"
        },
        {
            "id": str(uuid.uuid4()),
            "name": "Lanzhou Beef Noodle Soup",
            "posterId": "yuqi.guo17@gmail.com",
            "imageURL": "https://thewoksoflife.com/wp-content/uploads/2014/10/lanzhou-beef-noodle-soup-6.jpg",
            "content": "<h3 style=\"-webkit-text-stroke-width:0px;caret-color:rgb(0, 0, 0);color:rgb(0, 0, "
                       "0);font-style:normal;font-variant-caps:normal;letter-spacing:normal;orphans:auto;text-align"
                       ":start;text-decoration:none;text-indent:0px;text-transform:none;white-space:normal;widows"
                       ":auto;word-spacing:0px;\">Lanzhou Beef Noodle Soup Recipe</h3><h4 "
                       "style=\"-webkit-text-stroke-width:0px;caret-color:rgb(0, 0, 0);color:rgb(0, 0, "
                       "0);font-style:normal;font-variant-caps:normal;letter-spacing:normal;orphans:auto;text-align"
                       ":start;text-decoration:none;text-indent:0px;text-transform:none;white-space:normal;widows"
                       ":auto;word-spacing:0px;\">Ingredients:</h4><p "
                       "style=\"-webkit-text-stroke-width:0px;caret-color:rgb(0, 0, 0);color:rgb(0, 0, "
                       "0);font-style:normal;font-variant-caps:normal;font-weight:400;letter-spacing:normal;orphans"
                       ":auto;text-align:start;text-decoration:none;text-indent:0px;text-transform:none;white-space"
                       ":normal;widows:auto;word-spacing:0px;\"><strong>For the Broth:</strong></p><ul "
                       "style=\"-webkit-text-stroke-width:0px;caret-color:rgb(0, 0, 0);color:rgb(0, 0, "
                       "0);font-style:normal;font-variant-caps:normal;font-weight:400;letter-spacing:normal;orphans"
                       ":auto;text-align:start;text-decoration:none;text-indent:0px;text-transform:none;white-space"
                       ":normal;widows:auto;word-spacing:0px;\"><li>2 pounds beef shank or brisket</li><li>2 large "
                       "beef bones (preferably marrow bones)</li><li>2 large onions, quartered</li><li>4 slices of "
                       "ginger</li><li>4 cloves of garlic, crushed</li><li>2 star anise</li><li>1 cinnamon "
                       "stick</li><li>1 teaspoon Sichuan peppercorns</li><li>2 bay leaves</li><li>1 dried chili "
                       "pepper</li><li>2 tablespoons soy sauce</li><li>2 tablespoons Shaoxing wine (Chinese cooking "
                       "wine)</li><li>Salt to taste</li></ul><p "
                       "style=\"-webkit-text-stroke-width:0px;caret-color:rgb(0, 0, 0);color:rgb(0, 0, "
                       "0);font-style:normal;font-variant-caps:normal;font-weight:400;letter-spacing:normal;orphans"
                       ":auto;text-align:start;text-decoration:none;text-indent:0px;text-transform:none;white-space"
                       ":normal;widows:auto;word-spacing:0px;\"><strong>For the Noodles:</strong></p><ul "
                       "style=\"-webkit-text-stroke-width:0px;caret-color:rgb(0, 0, 0);color:rgb(0, 0, "
                       "0);font-style:normal;font-variant-caps:normal;font-weight:400;letter-spacing:normal;orphans"
                       ":auto;text-align:start;text-decoration:none;text-indent:0px;text-transform:none;white-space"
                       ":normal;widows:auto;word-spacing:0px;\"><li>1 pound fresh hand-pulled noodles or store-bought "
                       "Chinese wheat noodles</li></ul><p style=\"-webkit-text-stroke-width:0px;caret-color:rgb(0, 0, "
                       "0);color:rgb(0, 0, "
                       "0);font-style:normal;font-variant-caps:normal;font-weight:400;letter-spacing:normal;orphans"
                       ":auto;text-align:start;text-decoration:none;text-indent:0px;text-transform:none;white-space"
                       ":normal;widows:auto;word-spacing:0px;\"><strong>For the Garnishes:</strong></p><ul "
                       "style=\"-webkit-text-stroke-width:0px;caret-color:rgb(0, 0, 0);color:rgb(0, 0, "
                       "0);font-style:normal;font-variant-caps:normal;font-weight:400;letter-spacing:normal;orphans"
                       ":auto;text-align:start;text-decoration:none;text-indent:0px;text-transform:none;white-space"
                       ":normal;widows:auto;word-spacing:0px;\"><li>2 cups of thinly sliced daikon radish</li><li>2 "
                       "cups of chopped fresh cilantro</li><li>2 cups of chopped green onions</li><li>Fresh chili oil "
                       "to taste</li><li>White pepper to taste</li></ul><h4 "
                       "style=\"-webkit-text-stroke-width:0px;caret-color:rgb(0, 0, 0);color:rgb(0, 0, "
                       "0);font-style:normal;font-variant-caps:normal;letter-spacing:normal;orphans:auto;text-align"
                       ":start;text-decoration:none;text-indent:0px;text-transform:none;white-space:normal;widows"
                       ":auto;word-spacing:0px;\">Instructions:</h4><ol "
                       "style=\"-webkit-text-stroke-width:0px;caret-color:rgb(0, 0, 0);color:rgb(0, 0, "
                       "0);font-style:normal;font-variant-caps:normal;font-weight:400;letter-spacing:normal;orphans"
                       ":auto;text-align:start;text-decoration:none;text-indent:0px;text-transform:none;white-space"
                       ":normal;widows:auto;word-spacing:0px;\"><li><strong>Prepare the Broth:</strong> 1.1. Rinse "
                       "the beef shank/brisket and bones under cold water to remove any blood and impurities. 1.2. "
                       "Fill a large pot with water and bring it to a boil. Add the beef shank/brisket and bones. "
                       "Boil for about 5 minutes, then drain and rinse the meat and bones under cold water to remove "
                       "any scum. 1.3. Clean the pot, fill it with fresh water, and add the beef shank/brisket, "
                       "bones, onions, ginger, garlic, star anise, cinnamon stick, Sichuan peppercorns, bay leaves, "
                       "dried chili pepper, soy sauce, and Shaoxing wine. 1.4. Bring to a boil, then reduce to a "
                       "simmer. Cover and let it simmer for 2-3 hours until the beef is tender and the broth is "
                       "flavorful. Skim off any scum or fat that rises to the surface.</li><li><strong>Prepare the "
                       "Noodles:</strong> 2.1. If using fresh hand-pulled noodles, follow the instructions for "
                       "pulling and cooking them. If using store-bought noodles, cook them according to the package "
                       "instructions. Drain and rinse under cold water to stop the cooking "
                       "process.</li><li><strong>Prepare the Garnishes:</strong> 3.1. Thinly slice the daikon radish "
                       "and set aside. 3.2. Chop the fresh cilantro and green onions.</li><li><strong>Assemble the "
                       "Soup:</strong> 4.1. Remove the beef shank/brisket from the broth and slice it thinly. 4.2. "
                       "Strain the broth to remove the solids, returning the clear broth to the pot. Season with salt "
                       "to taste. 4.3. Divide the cooked noodles among serving bowls. 4.4. Top the noodles with "
                       "slices of beef, daikon radish, cilantro, and green onions. 4.5. Ladle the hot broth over the "
                       "noodles and garnishes. 4.6. Add fresh chili oil and white pepper to "
                       "taste.</li><li><strong>Serve Immediately:</strong> 5.1. Enjoy your homemade Lanzhou Beef "
                       "Noodle Soup while it's hot and flavorful.</li></ol><p "
                       "style=\"-webkit-text-stroke-width:0px;caret-color:rgb(0, 0, 0);color:rgb(0, 0, "
                       "0);font-style:normal;font-variant-caps:normal;font-weight:400;letter-spacing:normal;orphans"
                       ":auto;text-align:start;text-decoration:none;text-indent:0px;text-transform:none;white-space"
                       ":normal;widows:auto;word-spacing:0px;\">Great traditional food beef and noodle</p>"
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
