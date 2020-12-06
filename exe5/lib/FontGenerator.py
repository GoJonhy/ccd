from random import choices

class FontGenerator:
    def markovGeneretor(transationProb: float,state: int) -> int:
        prob_jump_previous_state=(transationProb/3);
        prob_jump_next_state=(transationProb/3);
        prob_stay_state=(transationProb/3);

        prob_double_jump_next_state=((1-transationProb)/2);
        prob_double_jump_previous_state=((1-transationProb)/2);
        jump_state=['previous','next','stay','double_previous','double_next'];
        probabilities=[prob_jump_previous_state,prob_jump_next_state,prob_stay_state,prob_double_jump_next_state,prob_double_jump_previous_state];

        step=''.join(choices(jump_state, probabilities));
        switcher = {
            'previous': state-1,
            'next': state+1,
            'stay': state,
            'double_previous': state-2,
            'double_next': state+2
        };
        state = switcher.get(step)
        print (state)
        if state < 0 :
            state =  state + 256;
        elif state > 255 :
            state =  state - 256;
        return state;