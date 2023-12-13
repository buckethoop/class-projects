;; This buffer is for text that is not saved, and for Lisp evaluation.
;; To create a file, visit it with C-x C-f and enter text in its buffer.

(defun merge-sorted-lists (list1 list2)
  (if (null list1)
      list2
      (if (null list2)
          list1
          (if (< (car list1) (car list2))
              (cons (car list1) (merge-sorted-lists (cdr list1) list2))
              (cons (car list2) (merge-sorted-lists list1 (cdr list2)))))))
