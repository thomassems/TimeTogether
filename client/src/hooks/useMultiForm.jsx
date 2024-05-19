import { useState } from "react";

export function useMultiform(steps) {
    const [currentStepIndex, setCurrentStepIndex] = useState(0)

    function next() {
        setCurrentStepIndex(i => {
            if (i >= steps.length - 1) return i
            return i + 1
        })
    }

    function back() {
        setCurrentStepIndex(i => {
            if (i<= 0) return i
            return i - 1
        })
    }

    function goTo(index) {
        setCurrentStepIndex(index)
    }


    return {
        currentStepIndex,
        step: steps[currentStepIndex],
        goTo,
        next,
        back,
        steps
    }
}