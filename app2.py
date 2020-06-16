from flask import Flask, jsonify, request
from http import HTTPStatus

app = Flask(__name__)

recipes = [
    {'id': 1,
     'name': 'Egg Salad',
    'description': 'This is a lovely egg salad recipe'},
    {
    'id': 2,
     'name': 'Tomato Pasta',
    'description': 'This is a lovely Tomato Pasta recipe'},
    {
     'id': 3,
     'name': 'DOsa',
    'description': 'This is a lovely Dosa recipe'}
]



@app.route('/recipes/', methods=['GET'])
def get_recipes():
    # print("Hello")
    return jsonify({'data': recipes})

@app.route('/recipes/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    recipe = next((recipe for recipe in recipes if recipe['id'] == recipe_id),None)

    if recipe:
         return jsonify(recipe)
@app.route('/recipes/', methods=['POST'])
def create_recipe():
    data = request.get_json()
    
    name = data.get('name')
    description = data.get('description')

    recipe = {
         'id' :  len(recipes) +1,
         'name': name,
         'description': description
    }
    recipes.append(recipe)

    return jsonify(recipes),HTTPStatus.CREATED

@app.route('/recipes/<int:recipe_id>', methods=['PUT'])
def update_recipe(recipe_id):
   recipe = next((recipe for recipe in recipes if recipe['id'] == recipe_id),None)
   if not recipe:
       return jsonify({'message': 'recipe not found'}),HTTPStatus.NOT_FOUND
   data = request.get_json()

   recipe.update(
       {
           'name' : data.get('name'),
           'description' : data.get('description')
       }
   )
   return jsonify(recipes)

@app.route('/recipes/<int:recipe_id>', methods=['DELETE'])
def Delete_recipe(recipe_id):
    for i in range(len(recipes)):
        if recipes[i]['id'] == recipe_id:
            del recipes[i]
            break
        else:

            return jsonify({'message': 'recipe not found'}),HTTPStatus.NOT_FOUND

    return jsonify(recipes)


# print(__name__)


if __name__ == "__main__":
    app.run()

