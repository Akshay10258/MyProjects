import { useState,useEffect } from 'react'
import Navbar from './components/navbar'
import { v1 as uuidv1 } from 'uuid';
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
// import './App.css'

function App()
{
  // const [todo, setTodo] = useState("");
  // creating a state for todos and intializing it with localstorage value if present else an empty array
  const [todos, setTodos] = useState(() => {
    const savedTodos = localStorage.getItem("myTodos");
    return savedTodos ? JSON.parse(savedTodos) : [];
  });

  const [text, setText] = useState("Enter New Todo");
  
  useEffect(() => {
    localStorage.setItem("myTodos", JSON.stringify(todos));
  }, [todos]);

  const handletext=(e) => {
    setText(e.target.value);
  }

  // ... is spread operator just spreads/short way of writing the array elements
  const addtodo=() => {
    if (text.trim()) {
      setTodos([...todos, { id: uuidv1(), text, iscompleted: false }]);
      setText("Enter New todo");
    }
  }
  const handleCheck=(e) => {
    // console.log(e.target.name);
    const targetid=e.target.name;
    const newTodos=[...todos];

    const ind=newTodos.findIndex((items) => {
      return items.id===targetid;
    }
    )
    newTodos[ind].iscompleted=!newTodos[ind].iscompleted;

    setTodos(newTodos); 
  }

  const handleDelete=(e) => {
    const targetid=e.target.name;
    const newTodos=[...todos];
    console.log(targetid)

    const ind=newTodos.findIndex((items) => {
      return items.id===targetid;
    }
    )

    newTodos.splice(ind,1);
    setTodos(newTodos); 
  }
  
  const handleEdit=(e) => {
    const targetid=e.target.name;
    console.log(targetid)
    const ind=todos.findIndex((items) => {
      return items.id===targetid;
    }
    )

    console.log("text",todos[ind].text)
    setText(todos[ind].text); //runs async
    todos.splice(ind,1);
    console.log(todos) //gets printed early
  }
  
  return (
    <>
      <Navbar/>
      <div className='bg-slate-400 flex items-center flex-col p-8 text-2xl h-[90vh]'>
        <input type="text" name="todo" id="todo" value={text} onChange={handletext} className='border-2 p-3 border-black rounded-lg h-10 w-1/2'/>
        <button onClick={addtodo} className='border-2 border-black m-5 rounded-lg w-1/12 bg-slate-100'>Enter</button>
      
        <div className="todos h-1/2">
          {todos.map(dos => {
            return <div key={dos.id} className='flex w-[80vw] justify-evenly'>
                <input type="checkbox" checked={dos.iscompleted} name={dos.id} id="input" onChange={handleCheck} className='w-[25px]'/>
                <span name={dos.id} className={dos.iscompleted?"line-through w-[35vw] flex items-center font-bold":"w-[35vw] flex items-center font-bold"}>{dos.text}</span>
                <button name={dos.id} onClick={handleEdit} className="edit border-2 border-black m-5 rounded-lg w-1/6 bg-slate-100 inline">Edit</button>
                <button name={dos.id} onClick={handleDelete} className="delete border-2 border-black m-5 rounded-lg w-1/6 bg-slate-100 inline">Delete</button>
              </div>
            }
          )}
        </div>
      </div>
    </>
  )
}

export default App
