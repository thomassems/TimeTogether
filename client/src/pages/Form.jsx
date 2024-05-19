
import { useMultiform } from "../hooks/useMultiForm"
import { useState } from "react"
import MyButton from '../components/MyButton'
import Landing from "./Landing"
import Creds from "./Creds"
import Hub from "./Hub"
import Sync from "./Sync"
import Contacts from "./Contacts"
import { motion, AnimatePresence } from 'framer-motion';

import {  Loader } from "../components/Loader";
 
const loadingStates = [
  {
    text: "Analyzing your calendar",
  },
  {
    text: "Calculating availibility",
  },
  {
    text: "Synchronizing events",
  },
  {
    text: "Fetching contact preferences",
  },
  {
    text: "Optimizing schedules",
  },
  {
    text: "Encrypting your data",
  },
  {
    text: "It's time!",
  },
];

const variants = {
    enter: { x: "100%", opacity: 0 },
    center: { x: 0, opacity: 1 },
    exit: { x: "-100%", opacity: 0 },
  };
  
  

function Form() {
    const [loading, setLoading] = useState(false);

    const [data, setData] = useState({
        firstName: "",
        lastName: "",
        password: "",
        calendar: "",
        contacts: [
            {
                name: "Jimmy Fang",
                priority: "3"
            }
        ],
    })

    const [completedForm, setCompletedForm] = useState('')
    const updateFields = (fields) => {
        setData(prev => {
            return {...prev, ...fields}
        })
    }

    const { step, steps, currentStepIndex, next} = useMultiform(
        [<Landing/>, <Creds {...data} updateFields={updateFields}/>, <Sync/>, <Contacts/>])

    function onSubmit(e) {
        e.preventDefault()
        if (currentStepIndex !== 3) return next()
        setLoading(true)
        setTimeout(() => {
            setLoading(false);
            setCompletedForm(true);
          }, 1); // Set a delay of 2 seconds
    }
  return (
    <>
        { completedForm ?
        <Hub data={data}/>
        :
        <form onSubmit={onSubmit}>

            {step}
            {currentStepIndex === 0 && <MyButton text={"Let's Get Started!"}/>}
            {currentStepIndex === 1 && <MyButton text={"Next: Sync Your Calendar"}/>}
            {currentStepIndex === 2 && <MyButton text={"Next: Choose Your Contacts"}/>}
            {currentStepIndex === 3 && <MyButton text={"Time Together!"}/>}
            <Loader loadingStates={loadingStates} loading={loading} duration={1500} />
        </form>
        }
    </>
  )
}

export default Form