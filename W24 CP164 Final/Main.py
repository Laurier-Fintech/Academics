from HSJ_Linked import List
from NDT_BST import BST

class TestLinked:

    def __init__ (self):
        """
        -------------------------------------------------------
        Initializes the TestLinked class and runs tests for the HSJ_Linked module.
        -------------------------------------------------------
        """
        gap(0)
        print("RUNNING/TESTING HSJ_LINKED BELOW: ")
        gap(0)
        self.use = List()
        self.points = 0
        self.testInsert()
        self.testExport()
        self.testRemove()
        self.testing = [4,2,5,1,0,0,2,2]
        eval(self.points, 28, "HSJ_LINKED")


    def testInsert (self):
        """
        -------------------------------------------------------
        Runs tests for the insert function of the List class.
        -------------------------------------------------------
        """
        print("\tTESTING INSERT FUNCTION")
        # Test cases for insertion
        tests = ["sIs ", "sIs jReally ", "hJason sIs jReally ", "hJason sIs jReally jCool ", "jGoddamn, jI sTreaple.jfeel jlike sApples.hApples.jthe sApples.jman. sPeaunuts.jFreshman jof jthe sOranges.jyear, sGrapes.jI jwoke jup jfeeling jlike jthe jman."]
        words = [
            [1,"Freshman ", 0],
            [1,"of ", 100],
            [1,"the ", 100],
            [1,"year, ", 100],
            [1, "I ", 100],
            [1,"woke ", 100],
            [1,"up ", 100],
            [1, "feeling ", 100],
            [1, "like ", 100],
            [1,"the ", 100],
            [1,"man.",100],
            [1,"Goddamn, ", 0],
            [1,"I ", 1],
            [1,"feel ", 2],
            [1,"like ", 3],
            [1,"the ", 4],
            [1, "man. ", 5],
            [0, "Apples.", 5],
            [0, "Oranges.", 10],
            [0, "Grapes.", 12],
            [0, "Peaunuts.", 7],
            [0, "Treaple.", 2],
            [2, "Apples.", 5],
            [0, "Apples.", 5],
        ]
        # Insertions and testing
        self.use.insert(0, "Is ",-100)
        self.points += test("Insert Blank",self.use.test(), tests[0], False, 2)
        self.use.insert(1, "Really ", 100)
        self.points += test("Insert Rear",self.use.test(), tests[1], False, 2)
        self.use.insert(2, "Jason ", 0)
        self.points += test("Insert Front",self.use.test(), tests[2], False, 2)
        self.use.insert(1, "Cool ", 3)
        self.points += test("Insert Full Rear", self.use.test(), tests[3], False, 2)
        self.use.clean()
        # Full quote insertion and testing
        for i in range(len(words)):
            self.use.insert(words[i][0], words[i][1], words[i][2])
        self.points += test("Insert Full Quote", self.use.test(), tests[4], False, 6)
        gap(2)
        print(f"\t\t\t {self.use.print()}")
        gap(2)

    def testExport(self):
        """
        -------------------------------------------------------
        Runs tests for the export function of the List class.
        -------------------------------------------------------
        """
        print("\tTESTING EXPORT FUNCTION")
        # Test cases for export
        tests = ["Goddamn, I feel like the the man. Freshman of the year, I woke up feeling like the man.", "Lauier Fintech is Really Cool And Awesome."]
        # Export tests
        self.points += test("Export Quote (Jump, Skip)", self.use.export(), tests[0], True, 6)
        self.use.clean()
        words = [
            [1, "Lauier ", 0],
            [0, "Hello ", 100],
            [2, "whoops ", 100],
            [0, "Fintech ", 100],
            [1, "is ", 100],
            [0, "Pineapple ", 100],
            [1, "Really ", 100],
            [2, "Hey ", 100],
            [2, "Cool ", 100],
            [0, "And ", 100],
            [1, "Awesome.", 100],
            [2, "Snowball.", 100],
        ]
        for i in range(len(words)):
            self.use.insert(words[i][0], words[i][1], words[i][2])
        # Export tests
        self.points += test("Export Quote (Hop, Skip, Jump)", self.use.export(), tests[1], True, 8)

    def testRemove(self):
        """
        -------------------------------------------------------
        Runs tests for the remove_skip function of the List class.
        -------------------------------------------------------
        """
        print("\tTESTING REMOVE FUNCTION")
        # Test cases for remove_skip
        tests = ["jLauier hwhoops jis jReally hHey hCool jAwesome.hSnowball.", "Hello Fintech Pineapple And "]
        # Remove skip and testing
        removed = self.use.remove_skip()
        self.points + test("Remove Skip (Check List) ", self.use.test(), tests[0], False, 4)
        test("Remove Skip (Check Removed) ", removed, tests[1], True, 4)

class TestBST:
    def __init__(self):
        """
        -------------------------------------------------------
        Initializes the TestBST class and runs tests for the Mock_BST module.
        -------------------------------------------------------
        """
        gap(0)
        print("RUNNING/TESTING NDT_BST BELOW: ")
        gap(0)
        self.use = BST()
        self.points = 0
        self.testInsert()
        self.testExists()
        self.testTotalNodes()
        self.testSiblings()
        self.testVein()
        self.testing = ["apple", "pace", "orange", "nana", "frump", "trick", "pit", "pif"]
        eval(self.points, 64, "NDT_BST")

    def testInsert(self):
        """
        -------------------------------------------------------
        Runs tests for the insert function of the BST class.
        -------------------------------------------------------
        """
        print("\tTESTING INSERT FUNCTION")
        checks = ["2", "21", "213", "1052176815121820"]
        tests = [10, 5, 15, 2, 7, 12, 18, 1, 6, 8, 20, 20, 10, 18]
        self.use.insert(2)
        self.points += test("Testing Root Insert", self.use.test(self.use._root), checks[0], False, 2)
        self.use.insert(1)
        self.points += test("Testing Left Insert", self.use.test(self.use._root), checks[1], False, 2)
        self.use.insert(3)
        self.points += test("Testing Right Insert", self.use.test(self.use._root), checks[2], False, 2)
        self.use = BST()
        for i in tests:
            self.use.insert(i)
        self.points += test("Inserting {10,5,15,2,7,12,18,1,6,8,20,20,10,18}", self.use.test(self.use._root), checks[3],False, 9)
        gap(2)
        self.use.print_bst(5)
        gap(2)

    def testExists(self):
        """
        -------------------------------------------------------
        Runs tests for the exists function of the BST class.
        -------------------------------------------------------
        """
        print("\tTESTING EXISTS FUNCTION")
        # Test cases for exists
        tests = [10, 20, 7, 3, 11]
        checks = [True, True, True, False, False]
        # Testing exists
        for i,x in enumerate(tests):
            self.points += test(f'Exists({x})', self.use.exists(self.use._root,x), checks[i], False, 1.2)

    def testTotalNodes(self):
        """
        -------------------------------------------------------
        Runs tests for the total_nodes function of the BST class.
        -------------------------------------------------------
        """
        print("\tTESTING TOTAL_NODES FUNCTION")
        # Test cases for total_nodes
        checks = [0,1,3,11]
        testOne = BST()
        self.points += test(f'TotalNodes (Empty)', testOne.total_nodes(), checks[0], False, 2)
        testOne.insert(2)
        self.points += test(f'TotalNodes (Root)', testOne.total_nodes(), checks[1], False, 2)
        testOne.insert(1)
        testOne.insert(3)
        self.points +=test(f'TotalNodes (Small Tree)', testOne.total_nodes(), checks[2], False, 2)
        self.points += test(f'TotalNodes (Big Tree)', self.use.total_nodes(), checks[3], True, 2)

    def testSiblings(self):
        """
        -------------------------------------------------------
        Runs tests for the siblings function of the BST class.
        -------------------------------------------------------
        """
        print("\tTESTING SIBLINGS FUNCTION")
        # Test cases for siblings
        tests = [[10,15], [5,15], [5,18],[30,40], [12, 18]]
        checks = [False, True, False, False, True]
        # Testing siblings
        for i,x in enumerate(checks):
            self.points +=test(f'Siblings({tests[i][0]},{tests[i][1]})', self.use.siblings(tests[i][0], tests[i][1]), x, False, 3)

    def testVein(self):
        """
        -------------------------------------------------------
        Runs tests for the find_vein function of the BST class.
        -------------------------------------------------------
        """
        print("\tTESTING VEIN FUNCTION")
        # Test cases for find_vein
        tests = [20,18,8,10,30]
        checks = [[10,15,18,20], [10,15,18],[10,5,7,8], [10], []]
        # Testing find_vein
        for i, x in enumerate(checks):
            self.points += test(f'Vein({tests[i]})', self.use.find_vein(tests[i]), x, True, 4)

def test(name, test, exp, show, points):
    """
    -------------------------------------------------------
    Evaluates a test and returns the points earned.
    -------------------------------------------------------
    Parameters:
        name - name of the test (str)
        test - result of the test (str)
        exp - expected result of the test (str)
        show - whether to display the test result (bool)
        points - points earned for the test (int)
    Returns:
        points earned for the test (int)
    -------------------------------------------------------
    """
    good = "CORRECT"
    if (test != exp):
        good = "INCORRECT"
        points = 0

    length = 50 - len(name)
    print(f"\t\t{name} -> {" " * length}{good}")
    if(show):
        print(f'\t\t\tEXPECTED: \"{exp}\"\n\t\t\tRESULT:   \"{test}\"')
    return points

def gap(tabs):
    """
    -------------------------------------------------------
    Prints a gap with a given number of tabs.
    -------------------------------------------------------
    Parameters:
        tabs - number of tabs (int)
    -------------------------------------------------------
    """
    out = ""
    for i in range(tabs):
        out += "\t"
    out += "-"*50
    print(out)

def eval(grd, max, name):
    """
    -------------------------------------------------------
    Evaluates and prints the final grade.
    -------------------------------------------------------
    Parameters:
        grd - earned grade (int)
        max - maximum possible grade (int)
        name - name of the class (str)
    -------------------------------------------------------
    """
    print("\n")
    print(f"\tThe {name} Class")
    gap(1)
    print(f"\tYOUR GRADE {grd}/{max}")
    print("\n")

print("THE CP164 MOCK MIDTERM - WINTER 2024\nCreated By: Laurier Fintech\nWritten By: Jason Van Humbeck\n")

a = TestLinked()
b = TestBST()
points = 0
gap(0)
print("BIG O NOTATION MC TEST:")
gap(0)
quiz = ["f(n) = n^2 + 200n + log(n) + 2000", "for (i = 0; i < n; i++){\n\tsum += i\n}", "for (i = 0; i < n; i++){\n\tfor (j = 0; j < n; j++){\n\t\tsum += 1\n\t}\n}", "f(n) = 100000000000 + 2000 + 10 + 2000", "Bubble Sort has a time complexity of O(n log n)", "Quick Sort has a time complexity of O(n log n)", "Selection Sort has a time complexity of O(n^2)", "Binary search is very effective, such that its time complexity can be represented by O(n)"]
for i,q in enumerate(quiz):
    print("\n\t" + q + "\n")
    if i < 4:
        print("\t\tSELECT THE BIG O NOTATION:\n\t\t\ta) O(1)\n\t\t\tb) O(log n)\n\t\t\tc) O(n)\n\t\t\td) O(n log n)\n\t\t\te) O(n^2)")
    else:
        print("\t\tIS THIS STATEMENT TRUE OR FALSE?\n\t\t\tt) TRUE\n\t\t\tf) FALSE")
    flip = True
    user_input = ''
    while(flip):
        user_input = input("\n\t\t -> ").strip().lower()
        if i < 4:
            if user_input in ['a', 'b', 'c', 'd', 'e']:
                flip = False
        if user_input in ['t', 'f']:
            flip = False
    if b.testing[i][a.testing[i]] == user_input:
        points += 1
eval(points, 8, "BIG O MC")
points += a.points + b.points
print(f"\n\n***YOUR OVERALL GRADE***\n\t{points}/100")

