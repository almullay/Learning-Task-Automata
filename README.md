# Learning-Task-Automata

Proof-of-concept implementation for theory in my Master's thesis, _Synthesising Reward Automata for Reinforcement Learning Using Hidden Markov Models_. Please find a pdf version for the mathematics and background here: https://almulla.files.wordpress.com/2022/04/ya_msc_thesis.pdf

To use:

`pip install pythomata`

1. Run `case_study.m`, `paper_case_study_3x3.m`, or `paper_case_study_4x4.m` in MATLAB.
2. Run `PMC2NFA(T_est, [L L L], (2*(grid_size^2)+1):(3*(grid_size^2)), "T_est_nfa")` in MATLAB.
3. Run `python3 cone_lumping.py T_est_nfa` from command line.
4. Run `python3 remove_bias.py T_est_nfa_cone_lumped a`.
5. Run `python3 remove_bias.py T_est_nfa_cone_lumped_lumped_by_a c`.
6. Run `python3 render_nfa.py T_est_nfa_cone_lumped_lumped_by_a_lumped_by_c` to generate an HTML visualization of the resulting finite-state machine (deterministic if learning was successful).
