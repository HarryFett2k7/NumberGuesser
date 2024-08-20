import streamlit as st
import random

#Title of the app
st.header("Number Guessing Game", divider="rainbow")
st.subheader("A simple number guessing game.")

#Initialize session state to store the random number and attempts

ask = st.text_input("What do you want the highest number to be?")
askint = int(ask)

if "random_number" not in st.session_state:
    st.session_state.random_number = random.randint(1, 10)
    st.session_state.attempts = 0

#User input for guessing the number
guess = st.number_input("Guess the number (between 1 and " + ask + "):", min_value=1, max_value=10, step=1)

#Button to submit the guess
if st.button("Submit Guess"):
    st.session_state.attempts += 1
    
    if guess < st.session_state.random_number:
        st.write("Too low.")
    elif guess > st.session_state.random_number:
        st.write("Too high.")
    else:
        st.write(f"Congratulations! You've guessed the number {st.session_state.random_number} correctly in {st.session_state.attempts} attempts.")
        if st.session_state.attempts == 1:
            st.write("You guessed it in 1, you are a master guesser!")
        elif st.session_state.attempts <= 3:
            st.write("You got it in 3 or less attempts, youre pretty good.")
        elif st.session_state.attempts <= 5:
            st.write("You got it in 5 or less attempts, youre alright.")
        elif st.session_state.attempts <= 7:
            st.write("You got it in 7 or less attempts, you should probably get better.")
        elif st.session_state.attempts <= 10:
            st.write("You got it in 10 or less attempts, how is this even possible??")

#Reset the game
if guess == st.session_state.random_number:
    if st.button("Play Again"):
        st.session_state.random_number = random.randint(1, 10)
        st.session_state.attempts = 0




else:
    st.write("Enter a guess and press 'Submit Guess'.")
