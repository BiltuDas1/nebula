from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import uuid
from models import Workspace
router = APIRouter()

# রিকোয়েস্ট বডির জন্য স্কিমা
class WorkspaceCreate(BaseModel):
    name: str
    password: str

# রিকোয়েস্ট বডির জন্য নতুন স্কিমা
class WorkspaceJoin(BaseModel):
    workspaceId: str
    password: str

@router.post("/join")
async def join_workspace(data: WorkspaceJoin):
    # আপাতত আমরা একটি সাকসেস মেসেজ রিটার্ন করছি 
    # (পরে এখানে ডাটাবেস চেক করার লজিক যোগ করা যাবে)
    
    workspace=await Workspace.filter(workspaceId=data.workspaceId, password=data.password).first()

    ##if data.password == "dev@123": # টেস্ট করার জন্য পাসওয়ার্ড চেক
    if workspace:
        return {
            "result": True,
            "message": "joined successfully"
        }
    else:
        # পাসওয়ার্ড ভুল হলে বা ওয়ার্কস্পেস না পেলে (Status 404)
        raise HTTPException(status_code=404, detail={
            "result": False,
            "message": "invalid password or workspace not found"
        })
    
@router.post("/new")
async def create_workspace(data: WorkspaceCreate):
    # একটি ইউনিক আইডি তৈরি করা
    unique_id = f"uuid-{str(uuid.uuid4())[:7]}-xyz"

    #add await
    await Workspace.create(workspaceId=unique_id, name=data.name, password=data.password)
    
    # আপনার আউটপুট ফরম্যাট (ইস্যু অনুযায়ী)
    return {
        "result": True,
        "message": "workspace created successfully",
        "data": {
            "workspaceId": unique_id
        }
    }