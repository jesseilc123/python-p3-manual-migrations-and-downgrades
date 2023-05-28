"""Renaming enrolled_date to enrolled_date_test

Revision ID: d9e8afa599fd
Revises: 791279dd0760
Create Date: 2023-05-28 13:36:20.258863

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd9e8afa599fd'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('students', 'enrolled_date', new_column_name='enrolled_date_test')


def downgrade() -> None:
    op.alter_column('students', 'enrolled_date_test', new_column_name='enrolled_date')
