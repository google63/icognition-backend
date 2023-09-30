"""Adding status column to Document

Revision ID: edf49b75908e
Revises: 3b83d6541e2d
Create Date: 2023-09-23 17:53:04.566528

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel
import pgvector
from pgvector.sqlalchemy import Vector


# revision identifiers, used by Alembic.
revision: str = 'edf49b75908e'
down_revision: Union[str, None] = '3b83d6541e2d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('document', sa.Column('status', sqlmodel.sql.sqltypes.AutoString(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('document', 'status')
    # ### end Alembic commands ###