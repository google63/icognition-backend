"""Add item vector and fixing non null fields

Revision ID: c8d0e0b0d608
Revises: 053941ff6d25
Create Date: 2023-08-20 11:58:34.382812

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel
import pgvector
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'c8d0e0b0d608'
down_revision: Union[str, None] = '053941ff6d25'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('wd_itemvector',
    sa.Column('text_vec', pgvector.sqlalchemy.Vector(dim=384), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('wikidata_id', sa.Integer(), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.alter_column('document', 'title',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('document', 'summary_generated',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('document', 'publication_date',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('document', 'publication_date',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.alter_column('document', 'summary_generated',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('document', 'title',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.drop_table('wd_itemvector')
    # ### end Alembic commands ###
