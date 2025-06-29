"""Add is_first_message column to chats

Revision ID: e3f249eef006
Revises: bebe2e2d3ee5
Create Date: 2024-11-12 15:56:53.596522

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'e3f249eef006'
down_revision = 'bebe2e2d3ee5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('chats', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_first_message', sa.Boolean(), nullable=True))
        batch_op.alter_column('session_id',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
        batch_op.drop_column('chat_metadata')
        batch_op.drop_column('code_snippet')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('chats', schema=None) as batch_op:
        batch_op.add_column(sa.Column('code_snippet', sa.TEXT(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('chat_metadata', postgresql.JSONB(astext_type=sa.Text()), autoincrement=False, nullable=True))
        batch_op.alter_column('session_id',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
        batch_op.drop_column('is_first_message')

    # ### end Alembic commands ###
