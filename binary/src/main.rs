use std::io;
use std::{num::ParseIntError};

fn main() -> Result<(), ParseIntError> {
    let mut binary = String::new();
    io::stdin()
        .read_line(&mut binary)
        .expect("Please input a binary string");

    // 7-bit or 8-bit ASCII
    if &binary.trim().len() % 8 == 0 {
        println!("{:?}", String::from_utf8(filter_out_backspace(decode_binary(&binary.trim(),8)?))); 
    }
    else {
        println!("{:?}", String::from_utf8(filter_out_backspace(decode_binary(&binary.trim(),7)?))); 
    }

    Ok(())
    
}

fn decode_binary(s: &str, n: usize) -> Result<Vec<u8>, ParseIntError> {
    (0..s.len())
        .step_by(n)
        // Convert binary chunk to ASCII
        .map(|i| u8::from_str_radix(&s[i..i + n], 2))
        .collect()
}

fn filter_out_backspace(mut xs: Vec<u8>) -> Vec<u8> {
    let index = xs.iter().position(|x| *x == 8).unwrap();
    // remove backspace key press
    xs.remove(index);
    // remove the key deleted by the backspace
    xs.remove(index-1);
    xs
}
