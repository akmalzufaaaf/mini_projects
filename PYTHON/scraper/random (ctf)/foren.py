# Sample moves in PGN format
moves_text = "g4 a6 c3 h6 Nf3 g5 Ne5 h5 Nc6 d6 Bh3 Ra7 Nxe7 Be6 Nxg8 b6 O-O Bxg4 e3 Kd7 Qxg4+ Kc6 Re1 Qd7 f3 Rh6 Bf1 Qd8 Qc8 Re6 Nh6 Rb7 Bb5+ Kxb5 Re2 Kc5 Kg2 Rg6 c4 Qf6 Kf2 Qh8 Qxc7+ Nc6 Kg3 Qh7 Qd8 d5 Nf5 b5 Qa5 f6 Kh3 Qh8 Qc7 Rxc7 Na3 Rb7 Rb1 bxc4 Ng3 Nb4 Nf1 Nc2 b4+ Kd6 Rb2 Ke7 f4 Rg7 Nxc4 Rd7 Ng3 Rg8 Rb3 Rd6 Kg2 Rd7 Ne4 Rg6 Re1 h4 fxg5 Qg8 Ne5 Kd8 Re2 Rd6 Nxf6 Ke7 Nf3 Kd8 Ng1 Rh6 a4 Qh7 Ra3 Qd3 Kh3 Rh5 Ng4 Qe4 b5 Qd4 Nh6 Qf4 bxa6 Ke8 Ng8 Rxa6 Ne7 Rc6 Nf3 Rc8 Nxc8 Qe5 Nb6 Qc3 Nc4 Qxe3 Ne5 Qe4 Rae3 Bb4 Nd7 Bc5 Rxe4+ Kxd7 Ne5+ Ke7 Nd3+ Kd7 Rf4 Rh7 Ba3 Rf7 Ne1 Kd8 Rf3 Rg7 Re7 Bxa3 Rff7 Nd4 Rf4 Nc2 Nxc2 Kc8 Re8+ Kc7 Re7+ Kd6 Rf2 Kc6 Rfe2 Kc5 Ra7 Rh7 Rc7+ Kb6 Ne1 Bc5 Rc8 Ka5 Rxc5+ Kb4 Rxd5 Rg7 Rd8 Kb3 Rd5 Kb4 Rd3 Rb7 Ra3 Rc7 Rb3+ Kc5 Nc2 Rd7 g6 Rd6 Rb7 Rd8 Kxh4 Rd7 Re1 Kd5 Re8 Rf7 Rf8 Ke6 Rd8 Rf5 Rb4 Re5 Re8+ Kd6 Na3 Rxe8 Kh5 Re4 Rb7 Rc4 Rb5 Ke7 Rc5 Kd6 Kh6 Rg4 Rc4 Kd7 Rc7+ Ke8 Rc4 Rh4+ Kg5 Rh8 Rc3 Rh5+ Kg4 Kf8 Kf4 Rh4+ Kg3 Rh3+ Kf4 Ke7 Ke5"

# Define ASCII mapping function
def map_to_ascii(move):
    file, rank = move[0], move[1]
    # Map file to ASCII (a=97, b=98, ..., h=104)
    file_ascii = ord(file)
    # Map rank to ASCII as an integer starting at 49 for '1'
    rank_ascii = ord(rank)
    return file_ascii + rank_ascii

# Convert each move to ASCII
ascii_text = ""
for move in moves_text.split():
    if len(move) >= 2:  # Skip moves like O-O for castling
        ascii_value = map_to_ascii(move[:2])
        ascii_text += chr(ascii_value)

# Print the ASCII text
print(ascii_text)
