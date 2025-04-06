import cachetools
from fastapi import APIRouter, HTTPException, Depends, UploadFile, File
from sqlalchemy.orm import Session
from app.models.post import Post
from app.models.user import User
from app.schemas.post_schema import PostCreate, PostResponse, PostListResponse
from app.core.db import SessionLocal, get_db
from app.services.auth_service import get_current_user


post_router = APIRouter()
cache = cachetools.TTLCache(maxsize=100, ttl=300)


@post_router.post("/addpost", response_model=PostResponse)
def add_post(post: PostCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """
    Add a new post (text) and return the post details (with postID).
    """
    # Validate payload size (limit 1 MB)
    if len(post.text.encode('utf-8')) > 1024 * 1024:
        raise HTTPException(status_code=400, detail="Payload size exceeds 1 MB")

    db_post = Post(text=post.text, user_id=current_user.id)

    db.add(db_post)
    db.commit()
    db.refresh(db_post)

    return db_post


@post_router.get("/getposts", response_model=PostListResponse)
def get_posts(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """
    Get all posts for the current user with caching for 5 minutes.
    """
    # Create a cache key based on the user ID (you can adjust this to fit your needs)
    cache_key = f"posts_user_{current_user.id}"

    # Check if the result is in cache
    if cache_key in cache:
        print("Getting from the cache")
        return PostListResponse(posts=cache[cache_key])

    # If not in cache, fetch from database
    posts = db.query(Post).filter(Post.user_id == current_user.id).all()

    # Store the result in cache
    cache[cache_key] = posts

    return PostListResponse(posts=posts)


@post_router.delete("/deletepost/{post_id}", response_model=PostResponse)
def delete_post(post_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """
    Delete a post by ID.
    """
    db_post = db.query(Post).filter(Post.id == post_id, Post.user_id == current_user.id).first()
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")

    db.delete(db_post)
    db.commit()

    return db_post
