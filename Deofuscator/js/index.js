// UTIL FUNCTIONS
function isDigit(c){
    return typeof c === "string" && c.length === 1 && c >= '0' && c <= '9';
}

function isValidPropertyName(s){
    // check if a given object may be a valid property name
    return typeof s === "string" && !isDigit(s.charAt(0)) && /[0-9a-zA-Z$_]+/.test(s);
}

function isLiteral(node){
    if(node.type === "ArrayExpression" && node.elements.length === 0){
        return true;
    }
    return node.type === "Literal";
}


// Transforms !![] and ![] !0, !7, etc into simpler values
function unaryExpression(node){
    if(node.type === "UnaryExpression"){
        if(isLiteral(node.argument)){
            let _node = {}
            _node.type = "Literal";
            _node.value = eval(node.operator + node.argument.raw);
            _node.raw = typeof _node.value === "string"? "'"+_node.value+"'":_node.value;
            return _node;
        }
    }
}

// Transforms 'h' +'ola' --> 'hola'
// Transform 3 - 1 --> 2
function binaryExpression(node){
    if(node.type === "BinaryExpression"){
        if(isLiteral(node.left) && isLiteral(node.right)){
            let _node = {};
            _node.type = "Literal";
            _node.value = eval(node.left.raw + node.operator + node.right.raw);
            _node.raw = typeof _node.value === "string"? "'"+_node.value+"'":_node.value;
            return _node;
        }
    }
}

function computedMemberExpression(node){
    if(node.type !== "MemberExpression") return;

    // object['length'] --> object.length
    if(node.computed && node.property.type === "Literal" && isValidPropertyName(node.property.value)) {
        let _node = {};
        _node.type = "MemberExpression";
        _node.computed = false;
        _node.object = node.object;
        _node.property = {
            type: "Identifier",
            name: node.property.value
        };
        _node.optional = node.optional;
        return _node;
    }
    // WARNING if first matches, second one will only be executed at next iteration
    // 'abc'[0] --> 'a'
    if(node.property.type === "Literal" && node.object.type === "Literal"){
        let _node = {};
        _node.type = "Literal";
        _node.value = eval(node.object.raw + '[' + node.property.raw + ']');
        _node.raw = typeof _node.value === "string"? "'"+_node.value+"'":_node.value;
        return _node;
    }
}


function negativeNumbers(node){
    if(isLiteral(node)){
        if(typeof node.value === "number" && node.value < 0){
            node.type = "UnaryExpression"
            node.operator = "-";
            node.argument = {type: "Literal", value: -node.value, raw: -node.value}
        }
    }
}

const transformationsToExecute = [unaryExpression, binaryExpression, computedMemberExpression];
const postProcessingToExecute = [negativeNumbers]

function deobfuscate(){
    let code = document.getElementById("input").value;
    let ast = esprima.parse(code);
    console.log(ast);
    let transformed_ast = applyTransformations(ast);
    console.log(transformed_ast);
    let transformed_code = escodegen.generate(transformed_ast);
    document.getElementById("output").value = transformed_code;
}

function applyTransformations(ast){
    let transformed = true;
    while (transformed){
        transformed = false;
        for (let i = 0; i < transformationsToExecute.length; i++) {
            let result = visit(ast, transformationsToExecute[i]);
            if(result){
                ast = result;
                transformed = true;
            }
        }
    }
    for (let i = 0; i < postProcessingToExecute.length; i++) {
        let result = visit(ast, postProcessingToExecute[i]);
        if(result){
            ast = result;
        }
    }
    return ast;
}


function visit(node, f){
    let changed = false;
    if (!node) {
        return;
    }
    let newNode = f(node);
    if(newNode){
        changed = true;
        node = newNode;
    }

    Object.keys(node).filter(key => {
        return typeof node[key] === "object";
    }).forEach((key, index) => {
        const value = node[key];
        if (Array.isArray(value)) {
            value.forEach((item, index) => {
                let newNode = visit(item, f);
                if(newNode){
                    changed = true;
                    value[index] = newNode;
                }
            });
        } else {
            let newNode = visit(value, f);
            if(newNode){
                changed = true;
                node[key] = newNode;
            }
        }
    });
    return changed? node: null;
}
