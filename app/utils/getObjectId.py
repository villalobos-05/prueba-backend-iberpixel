from bson import ObjectId
from fastapi import HTTPException, status


def getObjectId(id: str) -> ObjectId:
    """
    This is a dependency.

    Convert and return a string id to an mongo ObjectId.
    If id is not a valid ObjectId, an HTTP 400 error is raised.

    This is done because ids in Mongodb are handled with ObjectIDs,
    and, if a wrong id (id that cannot be converted to ObjectId) is given, it would throw and internal 500 error.
    """

    try:
        return ObjectId(id)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=f"Id {id} not valid"
        )
