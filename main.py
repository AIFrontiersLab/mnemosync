"""Mnemosync: A simple in-memory memory manager MVP."""
import time
from typing import Dict, Optional
from fastapi import FastAPI
from pydantic import BaseModel

class MemoryRequest(BaseModel):
    user_id: str
    content: str

class MemoryResponse(BaseModel):
    user_id: str
    content: str
    timestamp: float

class MemoryManager:
    def __init__(self):
        self.store: Dict[str, list] = {}

    def add_memory(self, user_id: str, content: str) -> MemoryResponse:
        entry = MemoryResponse(
            user_id=user_id,
            content=content,
            timestamp=time.time()
        )
        if user_id not in self.store:
            self.store[user_id] = []
        self.store[user_id].append(entry)
        return entry

    def get_memory(self, user_id: str) -> list:
        return self.store.get(user_id, [])

app = FastAPI(title="Mnemosync MVP")
manager = MemoryManager()

@app.post("/memories", response_model=MemoryResponse)
def create_memory(req: MemoryRequest):
    return manager.add_memory(req.user_id, req.content)

@app.get("/memories/{user_id}", response_model=list)
def get_memories(user_id: str):
    return manager.get_memory(user_id)

def demo():
    m = MemoryManager()
    res = m.add_memory("user_1", "I prefer dark mode")
    print(f"Added: {res.content}")
    retrieved = m.get_memory("user_1")
    print(f"Retrieved: {[r.content for r in retrieved]}")

if __name__ == "__main__":
    demo()