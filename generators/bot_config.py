# bot_config.py

# Quotas for each category
CATEGORY_QUOTAS = {
    "Popular": 50,
    "Backend": 40,
    "Functional": 30,
    "Systems": 25,
    "Scripting": 20,
    "Data_ML": 20,
    "Web_DSL": 20,
    "Other": 95
}

CATEGORIES = {
    "Popular": {
        "Python": {"ext": ".py", "run": "python {file}"},
        "JavaScript": {"ext": ".js", "run": "node {file}"},
        "Java": {"ext": ".java", "run": "javac {file} && java {name}"},
        "C++": {"ext": ".cpp", "run": "g++ {file} -o {name} && ./{name}"},
        "Go": {"ext": ".go", "run": "go run {file}"},
        "Rust": {"ext": ".rs", "run": "rustc {file} && ./{name}"},
        "TypeScript": {"ext": ".ts", "run": "ts-node {file}"},
    },
    "Backend": {
        "PHP": {"ext": ".php", "run": "php {file}"},
        "C#": {"ext": ".cs", "run": "csc {file} && ./{name}.exe"},
        "Ruby": {"ext": ".rb", "run": "ruby {file}"},
        "Swift": {"ext": ".swift", "run": "swift {file}"},
        "Kotlin": {"ext": ".kt", "run": "kotlinc {file} -include-runtime -d {name}.jar && java -jar {name}.jar"},
        "Scala": {"ext": ".scala", "run": "scala {file}"},
        "Dart": {"ext": ".dart", "run": "dart run {file}"},
        "Elixir": {"ext": ".exs", "run": "elixir {file}"},
    },
    "Functional": {
        "Haskell": {"ext": ".hs", "run": "runhaskell {file}"},
        "Clojure": {"ext": ".clj", "run": "clojure -M {file}"},
        "F#": {"ext": ".fsx", "run": "dotnet fsi {file}"},
        "Lisp": {"ext": ".lisp", "run": "sbcl --script {file}"},
        "OCaml": {"ext": ".ml", "run": "ocaml {file}"},
        "Erlang": {"ext": ".erl", "run": "erlc {file} && erl -noshell -s {name} start -s init stop"},
        "Scheme": {"ext": ".scm", "run": "guile -s {file}"},
        "Racket": {"ext": ".rkt", "run": "racket {file}"},
    },
    "Systems": {
        "C": {"ext": ".c", "run": "gcc {file} -o {name} && ./{name}"},
        "Zig": {"ext": ".zig", "run": "zig run {file}"},
        "Nim": {"ext": ".nim", "run": "nim c -r {file}"},
        "Assembly_x86": {"ext": ".asm", "run": "nasm -f elf64 {file} && ld {name}.o -o {name} && ./{name}"},
        "V": {"ext": ".v", "run": "v run {file}"},
        "D": {"ext": ".d", "run": "dmd -run {file}"},
        "Fortran": {"ext": ".f90", "run": "gfortran {file} -o {name} && ./{name}"},
    },
    "Scripting": {
        "Bash": {"ext": ".sh", "run": "bash {file}"},
        "PowerShell": {"ext": ".ps1", "run": "pwsh {file}"},
        "Perl": {"ext": ".pl", "run": "perl {file}"},
        "Lua": {"ext": ".lua", "run": "lua {file}"},
        "Tcl": {"ext": ".tcl", "run": "tclsh {file}"},
        "Rexx": {"ext": ".rexx", "run": "rexx {file}"},
    },
    "Data_ML": {
        "R": {"ext": ".R", "run": "Rscript {file}"},
        "Julia": {"ext": ".jl", "run": "julia {file}"},
        "MATLAB": {"ext": ".m", "run": "matlab -batch \"run('{file}')\""},
        "Wolfram": {"ext": ".wls", "run": "wolframscript -file {file}"},
        "SAS": {"ext": ".sas", "run": "sas {file}"},
    },
    "Web_DSL": {
        "HTML": {"ext": ".html", "run": "start {file}"},
        "CSS": {"ext": ".css", "run": "echo 'CSS'"},
        "SQL": {"ext": ".sql", "run": "echo 'SQL'"},
        "GraphQL": {"ext": ".gql", "run": "echo 'GraphQL'"},
        "YAML": {"ext": ".yaml", "run": "echo 'YAML'"},
        "React": {"ext": ".jsx", "run": "echo 'React'"},
        "Vue": {"ext": ".vue", "run": "echo 'Vue'"},
    },
    "Other": {
        "Solidity": {"ext": ".sol", "run": "solc {file}"},
        "Move": {"ext": ".move", "run": "move build"},
        "Cairo": {"ext": ".cairo", "run": "cairo-run --program {file}"},
        "WebAssembly": {"ext": ".wat", "run": "wasm-interp {file}"},
        "Ada": {"ext": ".adb", "run": "gnatmake {file} && ./{name}"},
        "COBOL": {"ext": ".cbl", "run": "cobc -x {file}"},
        "Pascal": {"ext": ".pas", "run": "fpc {file}"},
        "Smalltalk": {"ext": ".st", "run": "gst {file}"},
        "Groovy": {"ext": ".groovy", "run": "groovy {file}"},
        "Crystal": {"ext": ".cr", "run": "crystal run {file}"},
        "Hack": {"ext": ".hh", "run": "hh_client"},
        "Raku": {"ext": ".raku", "run": "raku {file}"},
        "BASIC": {"ext": ".bas", "run": "fbc {file}"},
        "Forth": {"ext": ".fs", "run": "gforth {file}"},
        "Awk": {"ext": ".awk", "run": "awk -f {file}"},
        "Sed": {"ext": ".sed", "run": "sed -f {file}"},
        "VHDL": {"ext": ".vhdl", "run": "ghdl {file}"},
        "Verilog": {"ext": ".v", "run": "iverilog {file}"},
        "Prolog": {"ext": ".pl", "run": "swipl {file}"},
    }
}

PROGRAM_TYPES = [
    "CLI Calculator", "TODO Manager", "File Processor", "Web Server", "Chat Bot",
    "Number Guessing Game", "Data Analysis Script", "REST API Client", "Unit Converter", "Task Scheduler",
    "Linked List Implementation", "Matrix Multiplication", "JSON Parser", "Markdown to HTML", "Fibonacci Sequence (Advanced)",
    "Tic Tac Toe", "Password Generator", "Log Analyzer", "Simple Encryption", "Weather Fetcher (Mock)"
]
