import {motion} from "framer-motion";

export function AnimatedDiv({
    children,
    variants,
    initial,
    animate,
    exit,
}){
    return (
        <motion.div
            variants = {variants}
            initial = {initial}
            animate = {animate}
            exit = {exit}
        >
            {children}
        </motion.div>
    );
}

export function FadedDiv({children}){

    const variants = {
        hidden: {
            opacity: 0
        },
        visible: {
            opacity: 1,
            transition: {
                duration: 0.3
            }
        },
        exit: {
            opacity: 0,
            transition: {
                duration: 0.3,
                ease: "easeInOut"
            }
        }
    }
    
    return (
        <AnimatedDiv
            variants = {variants}
            initial = {"hidden"}
            animate = {"visible"}
            exit = {"exit"}
        >
            {children}
        </AnimatedDiv>
    );
}
