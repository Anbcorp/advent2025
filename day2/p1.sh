cat 2_input | tr ',' '\n' | tr '-' ' ' | while read first last; do seq $first $last; done | sed -nE '/^([0-9]+)\1$/p' | awk '{sum+=$1;} END{print sum;}'
