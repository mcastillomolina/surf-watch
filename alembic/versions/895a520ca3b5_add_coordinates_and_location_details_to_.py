"""Add coordinates and location details to SurfSpot

Revision ID: 895a520ca3b5
Revises: 
Create Date: 2025-10-23 15:27:01.592050

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '895a520ca3b5'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Create all tables initially
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('email', sa.String(), nullable=True),
        sa.Column('phone_number', sa.String(), nullable=True),
        sa.Column('notifications_enabled', sa.Boolean(), nullable=True, server_default='true'),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_index(op.f('ix_users_name'), 'users', ['name'], unique=False)
    op.create_index(op.f('ix_users_phone_number'), 'users', ['phone_number'], unique=True)

    op.create_table(
        'surf_spots',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('location', sa.String(), nullable=True),
        sa.Column('latitude', sa.Float(), nullable=False),
        sa.Column('longitude', sa.Float(), nullable=False),
        sa.Column('country', sa.String(), nullable=True),
        sa.Column('continent', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_surf_spots_id'), 'surf_spots', ['id'], unique=False)
    op.create_index(op.f('ix_surf_spots_location'), 'surf_spots', ['location'], unique=False)
    op.create_index(op.f('ix_surf_spots_name'), 'surf_spots', ['name'], unique=False)

    op.create_table(
        'surf_reports',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('surf_spot_id', sa.Integer(), nullable=True),
        sa.Column('report_time', sa.DateTime(), nullable=True),
        sa.Column('wave_height', sa.String(), nullable=True),
        sa.Column('water_temperature', sa.String(), nullable=True),
        sa.Column('wind_speed', sa.String(), nullable=True),
        sa.Column('swell_direction', sa.String(), nullable=True),
        sa.ForeignKeyConstraint(['surf_spot_id'], ['surf_spots.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_surf_reports_id'), 'surf_reports', ['id'], unique=False)

    op.create_table(
        'user_surf_spots',
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('surf_spot_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['surf_spot_id'], ['surf_spots.id'], ),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('user_id', 'surf_spot_id')
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('user_surf_spots')
    op.drop_index(op.f('ix_surf_reports_id'), table_name='surf_reports')
    op.drop_table('surf_reports')
    op.drop_index(op.f('ix_surf_spots_name'), table_name='surf_spots')
    op.drop_index(op.f('ix_surf_spots_location'), table_name='surf_spots')
    op.drop_index(op.f('ix_surf_spots_id'), table_name='surf_spots')
    op.drop_table('surf_spots')
    op.drop_index(op.f('ix_users_phone_number'), table_name='users')
    op.drop_index(op.f('ix_users_name'), table_name='users')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
