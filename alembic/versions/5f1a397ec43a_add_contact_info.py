"""Add contact info

Revision ID: 5f1a397ec43a
Revises: bb2cf3e7cf0f
Create Date: 2023-08-09 21:59:55.953013

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5f1a397ec43a'
down_revision: Union[str, None] = 'bb2cf3e7cf0f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('insurances_patient_id_fkey', 'insurances', type_='foreignkey')
    op.create_foreign_key(None, 'insurances', 'patients', ['patient_id'], ['id'], source_schema='public', referent_schema='public')
    op.drop_constraint('referrals_patient_id_fkey', 'referrals', type_='foreignkey')
    op.create_foreign_key(None, 'referrals', 'patients', ['patient_id'], ['id'], source_schema='public', referent_schema='public')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'referrals', schema='public', type_='foreignkey')
    op.create_foreign_key('referrals_patient_id_fkey', 'referrals', 'patients', ['patient_id'], ['id'])
    op.drop_constraint(None, 'insurances', schema='public', type_='foreignkey')
    op.create_foreign_key('insurances_patient_id_fkey', 'insurances', 'patients', ['patient_id'], ['id'])
    # ### end Alembic commands ###
