"""
Views
"""

from flask import jsonify

from app import app
from models import Reward, User
from serializers import RewardSchema, UserSchema


# from flask import current_app
# from flask_appbuilder import ModelView
# from flask_appbuilder.models.sqla.interface import SQLAInterface


# @current_app.route('/')
@app.route('/')
def index():
    # return {}

    """The main endpoint"""
    # Get all users
    users = User.query.all()
    # users = User.query.paginate(page=1, per_page=2)
    users_schema = UserSchema(many=True)
    users_data = users_schema.dump(users)
    # Get rewards by user
    # user = users[1]
    # rewards = Reward.query.filter_by(user_id=user.id)
    # rewards_schema = RewardSchema(many=True)
    # rewards_data = rewards_schema.dump(rewards)
    return jsonify({'key': 'value',
                    'user': users_data})
                    # 'rewards': rewards_data})


# class GroupModelView(ModelView):
#     datamodel = SQLAInterface(User)
#     # related_views = [ContactModelView]

# class ContactModelView(ModelView):
#     datamodel = SQLAInterface(Contact)
#
#     label_columns = {'contact_group':'Contacts Group'}
#     list_columns = ['name','personal_cellphone','birthday','contact_group']
#
#     show_fieldsets = [
#         (
#             'Summary',
#             {'fields': ['name', 'address', 'contact_group']}
#         ),
#         (
#             'Personal Info',
#             {'fields': ['birthday', 'personal_phone', 'personal_cellphone'], 'expanded': False}
#         ),
#     ]

# appbuilder.add_view(
#     GroupModelView,
#     "List Groups",
#     icon = "fa-folder-open-o",
#     category = "Contacts",
#     category_icon = "fa-envelope"
# )
# appbuilder.add_view(
#     ContactModelView,
#     "List Contacts",
#     icon = "fa-envelope",
#     category = "Contacts"
# )
