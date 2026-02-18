import logging
from typing import Dict

from fastapi import APIRouter, Depends, HTTPException
from omni_python_library.dal.osint_data_access_layer import OsintDataAccessLayer
from omni_python_library.middleware.user_token import get_user_context
from omni_python_library.utils import NotFoundError, PermissionDeniedError

router = APIRouter(prefix="/delete", tags=["delete"])
logger = logging.getLogger(__name__)
dal = OsintDataAccessLayer()


@router.delete("/entity/{id:path}")
def delete_entity(id: str, user_ctx: Dict = Depends(get_user_context)):
    try:
        dal.delete_entity(id, user_ctx["user_id"], user_ctx["roles"])
        return {"status": "success", "id": id}
    except NotFoundError:
        raise HTTPException(status_code=404, detail="Entity not found or could not be deleted")
    except PermissionDeniedError:
        raise HTTPException(status_code=403, detail="Only the owner can delete this resource")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to delete entity {id}")
        raise HTTPException(status_code=500, detail="Internal service error")


@router.delete("/relation/{id:path}")
def delete_relation(id: str, user_ctx: Dict = Depends(get_user_context)):
    try:
        dal.delete_relation(id, user_ctx["user_id"], user_ctx["roles"])
        return {"status": "success", "id": id}
    except NotFoundError:
        raise HTTPException(status_code=404, detail="Relation not found or could not be deleted")
    except PermissionDeniedError:
        raise HTTPException(status_code=403, detail="Only the owner can delete this resource")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to delete relation {id}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
