
from coderl.main import CodeCompilerEnv
# from .main import CodeCompilerEnv
def test_basic_c_1():
    env = CodeCompilerEnv()
    code = """
    #include<stdio.h>
    int main(){
    printf("Hello World");
    return 0;
    }"""
    result = env.step(code)
    assert (result == (1, 1, True, {'stdout': 'Hello World'}))

def test_basic_c_2():
    env = CodeCompilerEnv()
    code = """
    #include<stdio.h>
    struct Point {
        int x, y;
    };
    int main(){
        if (1){
            printf("Hello World");
        }
        struct Point p = { 1 };  // Not initializing y will throw error in -Wextra
        printf("%d", p.x );
        return 0;
        }"""
    result = env.step(code)
    assert (result[:3] == (0, -1, True))
    #assert (result == (0, -1, True, {'stderr': 'temp_code.c: In function ‘main’:\ntemp_code.c:10:12: error: missing initializer for field ‘y’ of ‘struct Point’ [-Werror=missing-field-initializers]\n   10 |     struct Point p = { 1 };  // Not initializing y will throw error in -Wextra\n      |            ^~~~~\ntemp_code.c:4:12: note: ‘y’ declared here\n    4 |     int x, y;\n      |            ^\ncc1: all warnings being treated as errors\n'}))

def test_basic_c_3():
    env = CodeCompilerEnv()

    code = """
    #include<stdio.h>
    int main(){
        int x; // unused variable -Wall will trigger warning
        printf("Hello World");
        return 0;
        }"""
    result = env.step(code)
    assert (result[:3] == (0, -2, True))
    #assert (result == (0, -2, True, {'stderr': 'temp_code.c: In function ‘main’:\ntemp_code.c:4:9: error: unused variable ‘x’ [-Werror=unused-variable]\n    4 |     int x; // unused variable -Wall will trigger warning\n      |         ^\ncc1: all warnings being treated as errors\n'}))


def test_basic_c_4():
    env = CodeCompilerEnv()


    code = """
    #include<stdio.h>
    void foo(void){
        // int a = 2;
        return;
        }

    int main(){
        printf("Hello World");
        foo();

        // return 0;
        }
    """
    result = env.step(code)
    assert(result[:3] == (1, 1, True))
    assert(result == (1, 1, True, {'stdout': 'Hello World'}))

if __name__ == "__main__":
    test_basic_c_1()
    test_basic_c_2()
    test_basic_c_3()
    test_basic_c_4()

