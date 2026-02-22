import logging
from typing import Dict

from fastapi import APIRouter, Depends, HTTPException
from omni_python_library.dal import OsintDataAccessLayer, ViewDataAccessLayer
from omni_python_library.middleware import get_user_context
from omni_python_library.utils.errors import NotFoundError, PermissionDeniedError

router = APIRouter(prefix="/delete", tags=["delete"])
logger = logging.getLogger(__name__)
dal = OsintDataAccessLayer()
view_dal = ViewDataAccessLayer()


@router.delete("/entity/{id:path}", operation_id="delete_entity")
def delete_entity(id: str, user_ctx: Dict = Depends(get_user_context)):
    try:
        dal.delete_entity(id, user_ctx["user_id"], user_ctx["roles"])
        return {"status": "success", "id": id}
    except NotFoundError:
        logger.exception(f"User {user_ctx['user_id']} failed to delete entity {id} as it was not found")
        raise HTTPException(status_code=404, detail="Entity not found or could not be deleted")
    except PermissionDeniedError:
        logger.exception(f"User {user_ctx['user_id']} failed to delete entity {id} due to insufficient permissions")
        raise HTTPException(status_code=403, detail="Only the owner can delete this resource")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to delete entity {id}")
        raise HTTPException(status_code=500, detail="Internal service error")


@router.delete("/relation/{id:path}", operation_id="delete_relation")
def delete_relation(id: str, user_ctx: Dict = Depends(get_user_context)):
    try:
        dal.delete_relation(id, user_ctx["user_id"], user_ctx["roles"])
        return {"status": "success", "id": id}
    except NotFoundError:
        logger.exception(f"User {user_ctx['user_id']} failed to delete relation {id} as it was not found")
        raise HTTPException(status_code=404, detail="Relation not found or could not be deleted")
    except PermissionDeniedError:
        logger.exception(f"User {user_ctx['user_id']} failed to delete relation {id} due to insufficient permissions")
        raise HTTPException(status_code=403, detail="Only the owner can delete this resource")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to delete relation {id}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.delete("/view/{id:path}", operation_id="delete_view")
def delete_view(id: str, user_ctx: Dict = Depends(get_user_context)):
    try:
        view_dal.delete_view(id, user_ctx["user_id"], user_ctx["roles"])
        return {"status": "success", "id": id}
    except NotFoundError:
        logger.exception(f"User {user_ctx['user_id']} failed to delete view {id} as it was not found")
        raise HTTPException(status_code=404, detail="View not found or could not be deleted")
    except PermissionDeniedError:
        logger.exception(f"User {user_ctx['user_id']} failed to delete view {id} due to insufficient permissions")
        raise HTTPException(status_code=403, detail="Only the owner can delete this resource")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to delete view {id}")
        raise HTTPException(status_code=500, detail="Internal service error")
