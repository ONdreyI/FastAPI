from typing import Annotated
from fastapi import APIRouter, Path

router = APIRouter(prefix='/items', tags=['Items'])


@router.get('/')
def list_items():
    return [
        'Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5',
    ]


@router.get("/latest/")
def get_latest():
    return {'item': {'id': '0', 'name': 'latest'}}


@router.get('/{item_id}/')
def get_item_by_id(item_id: Annotated[int, Path(..., ge=1, lt=1_000_000)]):
    return {'item': {'id': item_id}}
