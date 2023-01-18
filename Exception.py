def main():

    try:

        print("Enter first  number")
        a = int(input())

        print("etner second number")
        b= int(input())

        c = a / b
        print("Division is:", c)

    except ZeroDivisionError:
        print("Inside zero division error")

    except ValueError:
        print("Inside Value Error")

    except Exception:
        print("Inside last exception block")

    finally:
        print("Inside finally block")

if __name__ == "__main__":
    main()