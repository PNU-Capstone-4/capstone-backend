"""empty message

Revision ID: 12baaf3095f3
Revises: 545980672560
Create Date: 2024-05-24 02:29:39.719314

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '12baaf3095f3'
down_revision = '545980672560'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Project', schema=None) as batch_op:
        batch_op.add_column(sa.Column('current_deploy_id', sa.Integer(), nullable=True))
        batch_op.drop_constraint('project_ibfk_2', type_='foreignkey')
        batch_op.create_foreign_key(None, 'Deploy', ['current_deploy_id'], ['id'])
        batch_op.drop_column('current_deployment_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Project', schema=None) as batch_op:
        batch_op.add_column(sa.Column('current_deployment_id', mysql.INTEGER(), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('project_ibfk_2', 'Deploy', ['current_deployment_id'], ['id'])
        batch_op.drop_column('current_deploy_id')

    # ### end Alembic commands ###
