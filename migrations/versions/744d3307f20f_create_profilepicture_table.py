"""Create ProfilePicture table

Revision ID: 744d3307f20f
Revises: f1ed9f2dda91
Create Date: 2024-04-02 11:12:54.193371

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '744d3307f20f'
down_revision = 'f1ed9f2dda91'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('profile_picture',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('picture_url', sa.String(length=255), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('profile_picture')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('profile_picture', sa.VARCHAR(length=255), nullable=True))

    op.drop_table('profile_picture')
    # ### end Alembic commands ###